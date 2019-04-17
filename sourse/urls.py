from sourse.users.controllers import UserRegistrationResource, UserAuthenticationResource
from sourse.posts.controllers import LikeResource, PostResource


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
        app.add_url_rule(
            '/post',
            view_func=PostResource.as_view('post'),
            methods=['POST'],
        )
        app.add_url_rule(
            '/like',
            view_func=LikeResource.as_view('like'),
            methods=['POST'],
        )

