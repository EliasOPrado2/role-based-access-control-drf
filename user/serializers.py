from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        fields = (
            'id',
            'last_login',
            'is_staff',
            'is_superuser',
            'first_name',
            'last_name',
            'username',
            'password',
            'groups',
            'email'
        )
        model = User
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validate_data):
        user = User.objects.create(**validate_data)
        user.set_password(validate_data['password'])
        user.is_staff = True
        user.save()

        return user