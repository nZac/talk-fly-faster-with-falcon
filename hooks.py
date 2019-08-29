import base64
import falcon


def check_auth_hook(req, resp, resource, params):
    if req.auth is None:
        raise falcon.HTTPForbidden()

    auth_type, secret = value.split(' ')
    return base64.b64decode(secret).decode().split(':')

    if self.parse_basic_auth(req.auth) != ['letmein', 'please']:
        raise falcon.HTTPForbidden()

@falcon.before(check_auth_hook)
class PrivateResource:
    def on_get(self, req, resp):
        resp.media = {'super': 'secret'}

class PublicResource:
    def on_get(self, req, resp):
        resp.media = {'hello': 'world'}

    @falcon.before(check_auth_hook)
    def on_post(self, req, resp):
        resp.media = {'requires': 'auth'}


api = falcon.API()
api.add_route('/public', PublicResource())
api.add_route('/private', PrivateResource())
