from functools import reduce
import utils


def create_html_element(
        html_element_type: str,
        content: str,
        classnames="",
        *html_attributes
) -> str:
    """
    Creates a html-element-string with content.
    :param html_element_type: The type of html-element you want to create, e.g. H1
    :param content: The children of the html element.
    :param classnames: optional classnames.
    :param html_attributes: Further attributes like ("style", "background-color: red")
    :return: The HTML-Element as a string.
    """
    classes = reduce(
        lambda clist, c: clist + c,
        classnames.split(";"),
        ' class="'
    ) + '"'

    attributes = " " + " ".join([
        f'{attr}="{val}"'
        for attr, val in html_attributes
    ])
    tag_opening = f'<{html_element_type}{classes if len(classnames) else ""}{attributes}>'
    tag_closing = f'</{html_element_type}>'

    return f"{tag_opening}{content}{tag_closing}"


def get_animals_template(animals: list[dict]) -> str:
    """
    Creates a html-list-item for each animal-list-item
    :param animals: list of animals
    :return: String of HTML-Elements (li-items).
    """
    return "\n".join(map(
        lambda animal: create_html_element(
            "li",
            utils.get_animal_data(animal),
            classnames="cards__item"
        ),
        animals
    ))


def create_error_message(search_string):
    return create_html_element(
        "h2",
        f'Sadly, the animal <strong>"{search_string}"</strong> doesn\'t exist (anymore).',
        classnames="error-message"
    )
