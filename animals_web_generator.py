from webbrowser import open as open_browser
import config
import utils


def main():
    """
    Loads the animals-data from the api-ninjas API as well as the html-data from the template.
    Replaces the template with generated data from the animals-data and saves it to animals.html.
    """
    # Fetch all animals, in this case foxes, from API
    animals = utils.fetch_animal("Fox")

    # Let the user choose a skin type
    skin_type = utils.prompt_for_skin_type(animals)

    # Select animals with matching skin-type
    filtered_animals = [
        animal
        for animal in animals
        if animal["characteristics"]["skin_type"] == skin_type
    ]

    # Create output template with selected animals
    template = utils.load_data(config.HTML_TEMPLATE, "html").replace(
        "__REPLACE_ANIMALS_INFO__",
        utils.get_animals_template(filtered_animals)
    )

    # Save template to file
    utils.save_data(template, config.HTML_OUTPUT_FILE, file_type="html")

    # Show results in browser
    open_browser(config.HTML_OUTPUT_FILE)


if __name__ == "__main__":
    main()
