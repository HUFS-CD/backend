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
    cctv_list = list(cctvs)
    my_array = []
    test_long = 127.06004762649577
    test_lat = 37.59644996896789
    end_lng = 127.0654903650288
    end_lat = 37.59585576408115
    
    while True:
        test_difference = []
        for cctv in cctv_list:
            g = math.sqrt(math.pow(float(cctv.latitude) - float(test_lat), 2) + math.pow(float(cctv.longtitude) - float(test_long), 2))
            h = math.sqrt(math.pow(float(cctv.latitude) - float(end_lat), 2) + math.pow(float(cctv.longtitude) - float(end_lng), 2))
            test_difference.append([cctv.id, g, cctv.address, cctv.latitude, cctv.longtitude, h])
        test_difference.sort(key=lambda x: x[1] + x[5])
        if float(test_difference[0][1]) - float(test_difference[0][5]) < 0.001:
            break
        else:
            test_long = test_difference[0][4]
            test_lat = test_difference[0][3]
            my_array.append(test_difference[0])
            del cctv_list[test_difference[0][0]]

    return render(request, 'mapapp/index.html', {'cctvs': my_array})

def main(request):
    cctvs = Cctv.objects.all()

    return render(request, 'mapapp/main.html', {'cctvs': cctvs})

class CctvList(generics.ListCreateAPIView):
    queryset = Cctv.objects.all()
    serializer_class = CctvSerializer

class CctvDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cctv.objects.all()
    serializer_class = CctvSerializer