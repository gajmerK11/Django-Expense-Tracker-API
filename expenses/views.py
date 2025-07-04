from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import serializers, viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer
from rest_framework.exceptions import PermissionDenied, NotFound


class RegisterSerializer(serializers.ModelSerializer):
    # Serializer to handle user registration data validation and creation
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Create a new user using Django's built-in create_user method (handles password hashing)
        user = User.objects.create_user(**validated_data)
        return user


class RegisterView(generics.CreateAPIView):
    # API view to register a new user (POST /auth/register/)
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class IsOwnerOrAdmin(permissions.BasePermission):
    # Custom permission to allow access only if user owns the object or is admin
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    # ViewSet to handle CRUD operations for ExpenseIncome mode
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        # Return all records for admin, or only the user's own records for regular users
        if self.request.user.is_staff:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=self.request.user)
    
    def get_object(self):
        # Get the object without filtering by user (so it always fetches if exists)
        obj = ExpenseIncome.objects.filter(pk=self.kwargs['pk']).first()
        if obj is None:
            raise NotFound(detail="ExpenseIncome not found.")

        # Check permissions manually
        if not (obj.user == self.request.user or self.request.user.is_staff):
            raise PermissionDenied(detail="You do not have permission to perform this action.")

        return obj

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the owner when creating a new record
        serializer.save(user=self.request.user)
