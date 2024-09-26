from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.token import get_tokens_for_user
from apps.users.models import User
from api.dto.users import CustomUserSerializer, CustomTokenObtainPairSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        tokens = get_tokens_for_user(user)
        
        user_data = CustomUserSerializer(user).data
        response_data = {
            'user': user_data,
            'tokens': tokens
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
