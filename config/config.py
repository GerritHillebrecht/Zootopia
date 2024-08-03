# File import paths
JSON_IMPORT_FILE = "animals_data.json"
HTML_TEMPLATE = "animals_template.html"
HTML_OUTPUT_FILE = "animals.html"

# Animal output data
DEFAULT_OUTPUT_KEYS: tuple = (
    {
        "field": "name",
        "display": "key",
        "elem_type": "div",
        "type": "headline"
    },
    {
        "field": "characteristics:slogan",
        "display": "val",
        "elem_type": "p",
        "type": "subline"
    },
    {
        "field": "characteristics:diet",
        "display": "key:value",
        "elem_type": "strong",
        "type": "description"
    }, {
        "field": "locations",
        "display": "key:value",
        "elem_type": "strong",
        "type": "description"
    }, {
        "field": "characteristics:type",
        "display": "key:value",
        "elem_type": "strong",
        "type": "description"
    },
)
