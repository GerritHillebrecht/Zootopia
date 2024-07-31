from functools import reduce
from config import DEFAULT_OUTPUT_KEYS


def get_animal_data(
        animal: dict,
        output_keys: tuple[str, ...] = DEFAULT_OUTPUT_KEYS
) -> str:
    """
    Creates a string of animal data, including all the selected data.
    :param animal: The animal data dictionary.
    :param output_keys: Select data to be printed by the animal keys. Use ":" for nesting.
    :return: The requested values a single string.
    """
    return "".join(
        # Output in "key: value" manner
        f'<span style="display: block">{key}: {value if type(value) is str else ", ".join(value)}</span>'
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
