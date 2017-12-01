from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def linearModel(request):
    if request.method == 'POST':
        print(request.body)
        received_json_data = json.loads(request.body)
    return HttpResponse("Hello, world. You're at the machinaLearning index." + str(received_json_data))
