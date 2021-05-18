from django.shortcuts import render
from .serializers import *
from .models import *
from .util import *
from rest_framework import serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
import json


class MonsterView(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer

class FighterSelectView(APIView):

     def post(self, request):
        
        fA = request.data[0]
        fighterA = Monster.objects.get(pk=fA)
        fB = request.data[1]
        fighterB = Monster.objects.get(pk=fB)
        
        fight_Log = fight(fighterA,fighterB)
        return Response(data=fight_Log, status=status.HTTP_200_OK) 
    