from sourse.users.controllers import UserRegistrationResource, UserAuthenticationResource


class Router:

    def add_routes(self, app):
        app.add_url_rule(
            '/user/registration',
            view_func=UserRegistrationResource.as_view('user'),
            methods=['POST'],
        )
        app.add_url_rule(
            '/user/auth',
            view_func=UserAuthenticationResource.as_view('auth'),
            methods=['POST'],
        )
