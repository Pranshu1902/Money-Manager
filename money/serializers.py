from rest_framework.serializers import ModelSerializer
from money.models import Transaction
from django.contrib.auth.models import User

# Serializers define the API representation.
class MoneySerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'spent', 'time']
    
    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

    # def validate(self, attrs):
    #     attrs['user'] = self.context['request'].user
    #     return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
