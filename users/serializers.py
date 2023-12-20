from django.contrib.auth.models import User, Permission, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # user_permissions = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Permission.objects.all(), many=True)
    # groups = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Group.objects.all(), many=True)

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'groups' in data:
            del data['groups']
        if 'user_permissions' in data:
            del data['user_permissions']
        return data
