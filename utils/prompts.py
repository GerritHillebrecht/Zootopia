def prompt_for_animal():
    """
    Prompts the user for the animal to be searched for.
    :return: The search string as str.
    """
    return input("Enter a name of an animal: ")


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
