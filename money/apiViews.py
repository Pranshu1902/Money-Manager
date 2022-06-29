from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from money.models import Transaction
from rest_framework.serializers import ModelSerializer

# Serializers define the API representation.
class MoneySerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'spent', 'time']

# install drf-spectacular to make the API swagger

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class MoneyViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = MoneySerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
