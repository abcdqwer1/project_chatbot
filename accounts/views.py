from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        request=UserSerializer,
        responses={200: UserSerializer},
        description='회원가입',)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)