from django.shortcuts import render
from django.http import JsonResponse
import json


def get_spider(request):
    ret = {'spider':{'name':'easy-spider', 'num':100, 'follow':True}}
    return JsonResponse(ret)
