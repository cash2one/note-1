from django.shortcuts import render
from django.http import JsonResponse
from .models import ImpApply
import json


def get_spider(request):
    imp_apply = ImpApply.objects.get(id=1)
    print type(imp_apply.json)
    # ret = {'spider':{'name':'easy-spider', 'num':100, 'follow':True}}
    return JsonResponse(imp_apply.json)
