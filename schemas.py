NAMES_CREATE = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-06/schema#",
  "$id": "http://names.com/root.json",
  "type": "object",
  "required": [
    "name"
  ],
  "properties": {
    "name": {
      "$id": "#/properties/name",
      "type": "string",
      "pattern": "^(.*)$"
    }
  }
}
