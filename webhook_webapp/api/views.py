# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def post(request):
    print("I got some JSON data:")
    print(request)

