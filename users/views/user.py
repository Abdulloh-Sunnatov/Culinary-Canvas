# users/views.py
import jwt
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers.user import (
    UserDeleteSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserProfileSerializer,
    UserRegisterSerializer,
    UserUpdateSerializer,
)
from users.tasks import ALGORITHM, SECRET_KEY


# ================= User Detail =================
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"



# ================= User Profile (Retrieve & Update) =================
class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # faqat o‘z profilini ko‘ra va update qilishi mumkin
        return self.request.user


# ================= User Registration =================
class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


# ================= Email Confirmation =================
class EmailConfirmAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user = User.objects.get(id=decoded.get("user_id"))
        except (User.DoesNotExist, jwt.ExpiredSignatureError, jwt.DecodeError):
            return Response(
                data={"detail": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.is_active = True
        user.is_confirmed = True
        user.save()

        return Response(data={"detail": "User confirmed"}, status=status.HTTP_200_OK)


# ================= User Logout =================
class UserLogoutAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        # logout qilayotgan userni o‘chiradi (yoki token blacklist qilinadi)
        instance = self.request.user
        instance.is_active = False
        instance.save()


# ================= User Update =================
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user.id != self.get_object().id:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Siz boshqa userni o‘zgartira olmaysiz.")
        serializer.save()
