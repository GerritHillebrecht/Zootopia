from webbrowser import open as open_browser
from functools import reduce
from config import JSON_IMPORT_FILE, HTML_TEMPLATE, HTML_OUTPUT_FILE, DEFAULT_OUTPUT_KEYS
from utils import load_data, save_data


def get_animal_data(
        animal: dict,
        output_keys: tuple[str, ...]
) -> str:
    """
    Creates a string of animal data, including all the selected data.
    :param animal: The animal data dictionary.
    :param output_keys: The selected data, defaults to name, type, diet, locations.
    :return: The requested values a single string.
    """
    return "".join(
        # Output in "key: value" manner
        f"{key}: {value if type(value) is str else ", ".join(value)}\n"
        for key, value in filter(
            # Check if key has value
            lambda zipped: zipped[1],

            # Zip the correct key with its value
            zip(
                map(lambda key_string: key_string.split(":")[-1].capitalize(), output_keys),
                map(lambda key_string: reduce(
                    lambda dictionary, key: dictionary.get(key),
                    key_string.split(":"),
                    animal
                ), output_keys)
            )
        )
    )


def get_animals_template_data(animals: list[dict]) -> str:
    return "\n".join(map(lambda animal: get_animal_data(animal, DEFAULT_OUTPUT_KEYS), animals))


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
