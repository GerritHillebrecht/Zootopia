import json


def load_data(file_path, file_type="json"):
    """ Loads the content of a file """
    with open(file_path, "r") as handle:
        if file_type == "json":
            return json.load(handle)
        return handle.read()


def save_data(data, file_path, file_type):
    """Saves content to a file"""
    with open(file_path, "w") as handle:
        if file_type == "json":
            return handle.write(json.dumps(data))
        handle.write(data)
