import falcon

class HelloWorldResource:
    def on_get(self, req, resp):
        resp.media = {"hello": "world"}

api = falcon.API()
api.add_route('/hello', HelloWorldResource())
