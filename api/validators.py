from rest_framework import serializers
# from .serializers import 


from.models import User

def validate_email(value):
    qs = User.objects.filter(email__exact = value)
    if qs.exists():
        raise serializers.ValidationError(f' account with email {value} already exixts')
    return value

def validate_password(value):
    if len(value) < 8:
        raise serializers.ValidationError('Passowrd is too short')
    try:
        password = int(value)
        raise serializers.ValidationError('Password should be amixture of letters and numbers')
    except:
        return value

    