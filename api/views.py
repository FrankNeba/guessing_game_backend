from django.shortcuts import render
from .serializers import CreateUser, ScoreSserializer, UpdateScoreSerializer
from rest_framework import generics, status 
from rest_framework.response import Response
from .models import User, Score
# Create your views here.


class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUser
    # pagination_class = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        score = Score(user = user)
        score.save()
        return Response(
            {'message':'User registered succesfully', 'user':serializer.data},
        )
    
class UpdateScore(generics.RetrieveUpdateAPIView):
    # queryset = Score.objects.all()
    serializer_class = UpdateScoreSerializer
    # lookup_field = 'user'

    def get_object(self):
        return Score.objects.get(user = self.request.user)

    def update(self, request, *args, **kwargs):

        instance = self.get_object()
        data = request.data.get('score', instance.score)
        if instance.highestScore < int(data):
            instance.highestScore = data
        instance.save()
        instance.score = data

        # new_score = request.data.get('score', instance.score)
        # if new_score > instance.highestScore:
        #     serializer.validated_data.hisghestScore = new_score
        # serializer.save()

        return Response(
            ScoreSserializer(instance).data
            # {'ok': 'wow'}
        )