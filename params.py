import falcon

class HelloWorldResource:
    def on_get(self, req, resp, name="world"):
        resp.media = {"hello": name}

api = falcon.API()
api.add_route('/hello', HelloWorldResource())
api.add_route('/hello/{name}', HelloWorldResource())
