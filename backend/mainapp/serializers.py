from rest_framework import serializers

from mainapp.models import User, ShortUrl
from mainapp.services import Key


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ('target_url', 'url')

        extra_kwargs = {
            'url': {'read_only': True}
        }

    def create(self, validated_data):
        url = ShortUrl(**validated_data)
        url.set_url(Key.get_secret())
        url.save()
        return url
