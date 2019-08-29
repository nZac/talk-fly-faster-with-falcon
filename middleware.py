import base64
import falcon


class AuthMiddleware:
    def parse_basic_auth(self, value):
        auth_type, secret = value.split(' ')
        return base64.b64decode(secret).decode().split(':')

    def process_resource(self, req, resp, resc, params):
        if not getattr(resc, 'auth_required', None):
            return

        if req.auth is None:
            raise falcon.HTTPForbidden()

        if self.parse_basic_auth(req.auth) != ['letmein', 'please']:
            raise falcon.HTTPForbidden()

class PrivateResource:
    auth_required = True

    def on_get(self, req, resp):
        resp.media = {'super': 'secret'}

class PublicResource:
    def on_get(self, req, resp):
        resp.media = {'hello': 'world'}


api = falcon.API(middleware=[AuthMiddleware()])
api.add_route('/public', PublicResource())
api.add_route('/private', PrivateResource())
