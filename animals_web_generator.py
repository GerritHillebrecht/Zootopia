from webbrowser import open as open_browser
from config import JSON_IMPORT_FILE, HTML_TEMPLATE, HTML_OUTPUT_FILE
from utils import load_data, save_data, get_animal_data, create_li_item


def get_animals_template_data(animals: list[dict]) -> str:
    return "\n".join(map(
        lambda animal: create_li_item(get_animal_data(animal)),
        animals)
    )


def main():
    """
    Loads the animals-data from the json-file as well as the html-data from the template.
    Replaces the template with generated data from the animals-data and saves it to animals.html.
    """
    animals = load_data(JSON_IMPORT_FILE)
    template = load_data(HTML_TEMPLATE, "html").replace(
        "__REPLACE_ANIMALS_INFO__",
        get_animals_template_data(animals)
    )
    save_data(template, HTML_OUTPUT_FILE, file_type="html")
    open_browser(HTML_OUTPUT_FILE)


if __name__ == "__main__":
    main()
