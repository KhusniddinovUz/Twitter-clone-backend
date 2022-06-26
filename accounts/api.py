from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from accounts.models import Accounts
from knox.models import AuthToken
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.conf import settings
import jwt


# All users
class AllUsers(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Accounts.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = RefreshToken.for_user(user).access_token
        url = f'http://127.0.0.1:8000/api/verify-email?token={str(token)}'
        email_body = f'Hi {user.username}. Please, click the link below to verify your TwitterCloneUz account. {url}'
        data = {'message': email_body, 'receiver': user.email}
        Util.send_email(data)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Verify Email
class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = Accounts.objects.get(id=payload['user_id'])
            user.email_verified = True
            user.save()
            return Response({'message': 'Email has been successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Activation Failed'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Recent users
class GetRecentUsers(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = Accounts.objects.order_by('-id')[:5]
    serializer_class = UserSerializer
