from webbrowser import open as open_browser
from config import JSON_IMPORT_FILE, HTML_TEMPLATE, HTML_OUTPUT_FILE
from utils import load_data, save_data, get_animal_data, create_html_element


def prompt_for_skin_type(animals: list[dict]) -> str:
    """
    Prompts the user to choose a skin-type.
    :param animals: All animal-data to prepare the available selection.
    :return: The chosen skin-type.
    """
    available_skin_types = set(sorted([
        animal["characteristics"]["skin_type"]
        for animal in animals
    ]))

    print("The animals can be divided by the following skin-types: ")
    for idx, skin_type in enumerate(available_skin_types):
        print(f'{idx + 1}. {skin_type}')

    while True:
        selected_skin = input("Select your purrrrrfect skin-type: ")
        if selected_skin in available_skin_types:
            return selected_skin
        print("Please choose a skin_type from the list above.")


def get_animals_template_data(animals: list[dict]) -> str:
    """
    Creates a html-list-item for each animal-list-item
    :param animals: list of animals
    :return: String of HTML-Elements (li-items).
    """
    return "\n".join(map(
        lambda animal: create_html_element(
            "li",
            get_animal_data(animal),
            classnames="cards__item"
        ),
        animals
    ))


def main():
    """
    Loads the animals-data from the json-file as well as the html-data from the template.
    Replaces the template with generated data from the animals-data and saves it to animals.html.
    """
    animals = load_data(JSON_IMPORT_FILE)
    skin_type = prompt_for_skin_type(animals)
    filtered_animals = [
        animal
        for animal in animals
        if animal["characteristics"]["skin_type"] == skin_type
    ]
    template = load_data(HTML_TEMPLATE, "html").replace(
        "__REPLACE_ANIMALS_INFO__",
        get_animals_template_data(filtered_animals)
    )
    save_data(template, HTML_OUTPUT_FILE, file_type="html")
    open_browser(HTML_OUTPUT_FILE)


if __name__ == "__main__":
    main()
