import falcon
from falcon.media.validators import jsonschema

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
      "pattern": "^(.*)$",
      "minLength": 1
    }
  }
}


from falcon.media.validators import jsonschema

class NamesResource:
    @jsonschema.validate(req_schema=NAMES_CREATE)
    def on_post_create(self, req, resp):
        resp.media = req.media

api = falcon.API()
api.add_route('/name', NamesResource(), suffix="create")
