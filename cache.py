import falcon
from falcon.media.validators import jsonschema
from collections import defaultdict

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


def four_oh_four_handler(req, resp, ex, params):
    resp.status = falcon.HTTP_404
    resp.media = {
        'title': 'Are you lost?',
        'description': 'Not all those who wander are lost.'
    }

class MissingNameError(falcon.HTTPNotFound):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def handle(req, resp, ex, params):
        resp.status = falcon.HTTP_404
        resp.media = {
            'title': f'Looking for {ex.name}?',
            'description': 'We don\'t know where that person is...'
        }

class NamesResource:
    def __init__(self):
        self.cache = defaultdict(int)

    def on_get_bare(self, req, resp):
        resp.media = self.cache

    @jsonschema.validate(req_schema=NAMES_CREATE)
    def on_post_bare(self, req, resp):
        name = req.media['name']
        self.cache[name] += 1
        resp.media = {'count': self.cache[name]}

    def on_get(self, req, resp, name):
        # Name is empty, e.g. `HTTP "/name/"`
        if not name or name not in self.cache:
            raise MissingNameError(name)

        resp.media = {
            "name": name,
            "count": self.cache[name]
        }

api = falcon.API()
api.add_error_handler(falcon.HTTPNotFound, four_oh_four_handler)
api.add_error_handler(MissingNameError)

names_resc = NamesResource()
api.add_route('/name', names_resc, suffix="bare")
api.add_route('/name/{name}', names_resc)
