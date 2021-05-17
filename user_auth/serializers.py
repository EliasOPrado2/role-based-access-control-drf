from rest_framework.serializers import ModelSerializer
from .models import UserAuth

class UserAuthSerializer(ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'groups',
            'email'
        )
        model = UserAuth
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validate_data):
        user_auth = UserAuth.objects.create(**validate_data)
        user_auth.set_password(validate_data['password'])
        user_auth.is_staff = True
        user_auth.save()

        return user_auth