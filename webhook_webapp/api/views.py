# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json

# Create your views here.

def post(request):
    print("I got some JSON data:")
    print(request)

