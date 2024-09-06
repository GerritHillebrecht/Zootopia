from webbrowser import open as open_browser
import config
import utils


def main():
    """
    Loads the animals-data from the api-ninjas API as well as the html-data from the template.
    Replaces the template with generated data from the animals-data and saves it to animals.html.
    """
    # Fetch animals from API, based on user selection
    animals = utils.fetch_animal(
        # API handles case-sensitivity, no need to make it lower-case.
        utils.prompt_for_animal()
    )

    # Removed the prompt for skin-typs for now, maybe it's still needed later on
    # # Let the user choose a skin type
    # skin_type = utils.prompt_for_skin_type(animals)
    #
    # # Select animals with matching skin-type
    # filtered_animals = [
    #     animal
    #     for animal in animals
    #     if animal["characteristics"]["skin_type"] == skin_type
    # ]

    # Create output template with selected animals
    template = utils.load_data(config.HTML_TEMPLATE, "html").replace(
        "__REPLACE_ANIMALS_INFO__",
        utils.get_animals_template(animals)
    )

    # Save template to file
    utils.save_data(template, config.HTML_OUTPUT_FILE, file_type="html")
    print(f"Website was successfully generated to the file {config.HTML_OUTPUT_FILE}.")

    # Show results in browser
    open_browser(config.HTML_OUTPUT_FILE)


if __name__ == "__main__":
    main()
