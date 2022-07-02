from django.contrib.auth.models import User
# from requests import Response
from rest_framework import viewsets
from money.models import Transaction
from rest_framework.serializers import ModelSerializer

# Serializers define the API representation.
class MoneySerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'spent', 'time']
        read_only_fields = ['user']

    # automatically assign the user to the transaction
    def validate(self, attrs):
        user = User.objects.filter(username=self.context['request'].user)[0]
        attrs['user'] = user
        return attrs

# install drf-spectacular to make the API swagger

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    # sign up new user
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class MoneyViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = MoneySerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


#@api_view(['GET'])
#def current_user(request):
#    serializer = UserSerializer(request.user)
#    return Response(serializer.data)


class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
