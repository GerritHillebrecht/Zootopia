from functools import reduce
from config import DEFAULT_OUTPUT_KEYS
from .serialization import create_html_element


def get_animal_data(
        animal: dict,
        selected_keys: tuple[dict] = DEFAULT_OUTPUT_KEYS
) -> str:
    """
    Creates a string of animal data, including all the selected data.
    :param animal: The animal data dictionary.
    :param selected_keys: Select data to be printed by the animal keys. Use ":" for nesting.
    :return: The requested values as a single string.
    """

    # Get all different types of output-types, like headline and description
    unique_output_types = set(key["type"] for key in selected_keys)

    # Match the value of the actual key to the capitalized key.
    # This is necessary, since we're accessing by nested strings, e.g. "characteristics:type".
    matched_key_values = list(filter_empty_values(
        match_key_val(animal, [key_data["field"] for key_data in selected_keys])
    ))

    # Dictionary of the different output types matched to the animal data of that type.
    dict_type_to_rendered_strings = {
        u_type: [
            # Create html-string based on the type
            render_output_line(
                matched_key_values[idx][0],
                matched_key_values[idx][1],
                selected_keys[idx]
            )
            for idx in range(len(matched_key_values))
            if selected_keys[idx]["type"] == u_type
        ]
        for u_type in unique_output_types
    }

    # Create a custom html-element for every type.
    return "".join([
        # Headline elements
        create_html_element(
            "div",
            "".join(dict_type_to_rendered_strings["headline"]),
            classnames="card__title"
        ),
        create_html_element(
            "p",
            "".join(dict_type_to_rendered_strings["description"]),
            classnames="card__text"
        )
    ])


def match_key_val(input_dictionary, key_strings) -> tuple[tuple[str, str]]:
    """
    Extracts the nested key and matches it the according value.
    :param input_dictionary: The Data to extract from, in this case the individual animal.
    :param key_strings: The nested key string, e.g. "characteristics:type".
    :return: A tuple of tuples, with the formatted and matched keys and values.
    """
    return zip(
        map(
            lambda key_string: key_string.split(":")[-1].capitalize(),
            key_strings
        ),
        map(
            lambda key_string: reduce(
                lambda dictionary, key: dictionary.get(key),
                key_string.split(":"),
                input_dictionary
            ), key_strings
        )
    )


def filter_empty_values(iterable):
    """
    Checks for each item of the iterable if it has a value for its key.
    :param iterable: A list of tuple of tuples.
    :return: A filtered selection.
    """
    return filter(
        # Check if key has value
        lambda zipped: zipped[1],

        # Zip the correct key with its value
        iterable
    )


def combine_list(value, list_connector=", "):
    """
    Connects a list if it isn't already a string
    :param value: The list to be connected.
    :param list_connector: The symbol to connect your list with
    :return: The connected list as a string.
    """
    return list_connector.join(value) if type(value) is list else str(value)


def render_output_line(key, value, data):
    """
    Renders depending on the output_type the string.
    :param key: Key of the key-value pair to be output.
    :param value: Value of the key-value pair to be output.
    :param data: The whole dictionary.
    :return: HTML-ELement.
    """
    if data["type"] == "headline":
        return value

    key = create_html_element(data["elem_type"], key)
    content = combine_list(value)
    return f'{key}: {content}<br />'
