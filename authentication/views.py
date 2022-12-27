from rest_framework import response, status
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializers


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
