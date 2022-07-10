from django.http import HttpResponseRedirect
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from mainapp.models import User, ShortUrl
from mainapp.serializers import UserSerializer, UrlSerializer
from mainapp.services import UserUrl


class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UrlViewSet(viewsets.GenericViewSet,
                 mixins.CreateModelMixin):
    queryset = ShortUrl.objects.all()
    serializer_class = UrlSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()
        UserUrl.set_url_to_user(url, request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=('GET',), detail=False)
    def my_urls(self, request, pk=None):
        urls = UserUrl.get_all(request.user)
        return Response(urls)


def redirect_to(request, url):
    obj = ShortUrl.objects.get(url=url)
    return HttpResponseRedirect(redirect_to=obj.target_url)
