import secrets

from mainapp.models import User, ShortUrl


class Key:
    @staticmethod
    def get_secret():
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "".join(secrets.choice(chars) for _ in range(5))
        return key


class UserUrl:
    @staticmethod
    def set_url_to_user(url: ShortUrl, user: User):
        u = User.objects.get(email=user)
        u.urls.add(url)
        u.save()

    @staticmethod
    def get_all(user: User):
        u = User.objects.get(email=user)
        return {'my_urls': u.urls.values_list()}
