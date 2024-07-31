# File import paths
JSON_IMPORT_FILE = "animals_data.json"
HTML_TEMPLATE = "animals_template.html"
HTML_OUTPUT_FILE = "animals.html"

# Animal output data
DEFAULT_OUTPUT_KEYS: tuple[str, ...] = (
    "name",
    "characteristics:diet",
    "locations",
    "characteristics:type"
)
