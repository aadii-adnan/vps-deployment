from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from .filters import ProductFilter
from .pagination import ProductPagination

from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token


from .models import Product
from .serializers import ProductSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class productviewsets(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_class = ProductFilter

    pagination_class = ProductPagination

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class RegisterView(APIView):

    def post(self, request):

        serializer = UserSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message":
                    "User Registered Successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            token, created = Token.objects.get_or_create(
                user=user
            )

            return Response(
                {
                    "token": token.key
                }
            )

        return Response(
            {
                "error":
                "Invalid Credentials"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
# Create your views here.
