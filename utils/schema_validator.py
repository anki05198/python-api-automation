import json
from jsonschema import validate


def validate_json_schema(data, schema_file):
    with open(schema_file) as file:
        schema = json.load(file)

    validate(instance=data, schema=schema)