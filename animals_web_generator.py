import json

JSON_FILE_NAME = "animals_data.json"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals(
        animals: list[dict],
        specific_keys=("name", "characteristics:diet", "locations", "characteristics:type")
):
    """
    Prints the specified data for animals in given list.
    :param animals: List of animals to print.
    :param specific_keys: The data to print of each animal. Use ":" for nested data.
    :type specific_keys: tuple[str]
    :returns: Prints the animals, no output.
    """
    for animal in animals:
        for keys in specific_keys:
            value = animal
            for key in keys.split(":"):
                value = value.get(key)
            if value:
                animal_key = keys.split(":")[-1].capitalize()
                animal_value = value if type(value) is str else value[0]
                # Would be better to just join the list, but the assignment requires the
                # first element.
                # animal_value = value if type(value) is str else ", ".join(value)
                print(f"{animal_key}: {animal_value}")
        print("")


def main():
    """
    Load the animals-data from the json-file and prints it.
    """
    animals_data = load_data(JSON_FILE_NAME)
    print_animals(animals_data)


if __name__ == "__main__":
    main()
