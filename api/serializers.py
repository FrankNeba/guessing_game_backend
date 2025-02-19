from rest_framework import serializers
from .models import User, Score
from .validators import validate_password, validate_email
from rest_framework.permissions import IsAuthenticated


# from django.contrib.auth.password_validation import validate_password
# from rest_framework.validators import UniqueValidator


class CreateUser(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [validate_email]
    )

    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )

    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'passowrd': 'Passwords don\'t match.'})
        return data
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    

class ScoreSserializer(serializers.ModelSerializer):
    # discount = serializers.CharField()
    username = serializers.SerializerMethodField()
    highestScore = serializers.SerializerMethodField()
    class Meta:
        model = Score
        fields = [
            'score',
            'highestScore',
            'username'
            ]
    
    def get_username(self, value):
        return value.user.username
    
    def get_highestScore(self, obj):
        return obj.highestScore
    # def update(self, instance, validated_data):
    #     instance.score = validated_data.get('score', instance.score)
    #     instance.save()
    #     return instance
    # def get_hishestScore (self, value):
    #     if value.score > value.hisghestScore:
    #         return value.score
    #     return value.highestScore
    
    # def create(self, validated_data):
    #     obj = Score.create(
    #         name = validated_data.get('user'),
    #         defaults = {'score':validated_data.get('score', '')}
    #     )

    #     return obj

class UpdateScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['score']
        
