from django.shortcuts import render

# Create your views here.

#api endpoint to create a tok
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Tok
from .serializers import TokSerializer

#create a tok
@csrf_exempt
def create_tok(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TokSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#list all toks
@csrf_exempt
def list_toks(request):
    if request.method == 'GET':
        toks = Tok.objects.all()
        serializer = TokSerializer(toks, many=True)
        return JsonResponse(serializer.data, safe=False)

#retrieve, update, or delete a tok
@csrf_exempt
def tok_detail(request, pk):
    try:
        tok = Tok.objects.get(pk=id)
    except Tok.DoesNotExist:
        return HttpResponse(status=404, content="Tok not found")

    if request.method == 'GET':
        serializer = TokSerializer(tok)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TokSerializer(tok, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tok.delete()
        return HttpResponse(status=204)
