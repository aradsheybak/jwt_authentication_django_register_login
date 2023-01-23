from rest_framework.serializers import ModelSerializer
from User.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'mobile', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            mobile=validated_data['mobile'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

