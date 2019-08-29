import falcon

class NamesResource:
    def on_get(self, req, resp, name=None):
        resp.media = {"hello": name}

    def on_get_list(self, req, resp):
        resp.media = [
            {"name": "Amy"}, {"name": "Bob"},
            {"name": "Claire"}, {"name": "Tucker"},
        ]

api = falcon.API()
api.add_route('/name', NamesResource(), suffix="list")
api.add_route('/name/{name}', NamesResource())
