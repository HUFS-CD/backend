import logging
import math

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from mapapp.models import Cctv
from mapapp.serializers import CctvSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response


def index(request):
    cctvs = Cctv.objects.all()
    test_difference= []
    five_difference= []
    test_long = 127.06004762649577
    test_lat = 37.59644996896789


    for cctv in cctvs:
        test_difference.append([cctv.id, math.sqrt(math.pow(float(cctv.latitude) - test_lat, 2) + math.pow(float(cctv.longtitude) - test_long, 2)), cctv.address])

    test_difference.sort(key=lambda x: x[1])
    test_difference = test_difference[:5]

    return render(request, 'mapapp/index.html', {'cctvs': test_difference})


class CctvList(generics.ListCreateAPIView):
    queryset = Cctv.objects.all()
    serializer_class = CctvSerializer

class CctvDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cctv.objects.all()
    serializer_class = CctvSerializer