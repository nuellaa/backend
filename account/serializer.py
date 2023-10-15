from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class userCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):

        user = User.objects.filter(email = data['email']).first()
        
        if(data['first_name'] == "" or data['last_name'] == "" or data['email'] == ""):
            raise ValueError("Input fields cannot be empty")
        
        elif user is not None:
            raise ValueError("Email Already Exists")
        
        else:
            return data
    
    def create(self, data):
        pwd = data['password']

        encrypted_pwd = make_password(pwd, "fnlwenilqanlakxqlkkamxka")

        new_user = User.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            username = data['username'],
            password = encrypted_pwd
        )

        return new_user

        


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def login(self, data):
        
        verify_user = User.objects.filter(email = data['email']).first()
        
        if verify_user is None:
            raise ValueError("Invalid Credentials")
        else:
            encrypted_pwd = getattr(verify_user, "password")
            check = check_password(data['password'], encrypted_pwd)

            if check == True:
                data = {
                    "id": getattr(verify_user, "id"),
                    "first_name": getattr(verify_user, "first_name"),
                    "last_name": getattr(verify_user, "last_name")

                }
                return data
            else:
                raise ValueError("Invalid Credentials")