import falcon

class HelloWorldResource:
    def on_get(self, req, resp):
        resp.media = {"hello": "world"}

def create_app():
    api = falcon.API()
    api.add_route('/hello', HelloWorldResource())
    return api

api = create_app()
