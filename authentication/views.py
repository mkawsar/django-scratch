from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import response, status, permissions

from authentication.serializers import AuthUserSerializers, LoginSerializers, RegisterSerializers


# Create your views here.
class RegisterAPIView(GenericAPIView):
    authentication_classes = []
    serializer_class = RegisterSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_412_PRECONDITION_FAILED)


class LoginAPIView(APIView):
    serializer_class = LoginSerializers
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.data['email'], password=request.data['password'])
        if user:
            serializer = self.serializer_class(user)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return response.Response({'data': 'Invalid credentials, try again'}, status=status.HTTP_401_UNAUTHORIZED)


class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        print(user.groups.filter(name='user').exists())
        serializer = AuthUserSerializers(user)
        return response.Response({'data': serializer.data, 'status': status.HTTP_200_OK})
