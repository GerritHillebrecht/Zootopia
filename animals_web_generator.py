import os
from webbrowser import open as open_browser
import utils
import data_fetcher


def main():
    """
    Loads the animals-data from the api-ninjas API as well as the html-data from the template.
    Replaces the template with generated data from the animals-data and saves it to animals.html.
    """

    # Prompt user for animal
    search_string = utils.prompt_for_animal()

    # Fetch animals from API, based on user selection
    animals = data_fetcher.fetch_data(
        # API handles case-sensitivity, no need to make it lower-case.
        search_string
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
    template = utils.load_data(os.getenv("HTML_TEMPLATE"), "html").replace(
        "__REPLACE_ANIMALS_INFO__",
        utils.get_animals_template(animals) if len(animals) > 0
        else utils.create_error_message(search_string)
    )

    # Save template to file
    html_output_file = os.getenv("HTML_OUTPUT_FILE")
    utils.save_data(template, html_output_file, file_type="html")
    print(f"Website was successfully generated to the file {html_output_file}.")

    # Show results in browser
    open_browser(html_output_file)


if __name__ == "__main__":
    main()
