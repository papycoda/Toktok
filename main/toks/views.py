from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from fastapi import FastAPI
from fastapi import Response
from pydantic import BaseModel
from .models import Toks
from .serializers import TokSerializer

app = FastAPI()

class TokRequest(BaseModel):
    tok: str

#create a tok
@csrf_exempt
@app.post("/toks/") #this is the route for the endpoint that will be created 
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
@app.get("/toks/")
def list_toks(request):
    #list all toks
    toks = Toks.objects.all()
    serializer = TokSerializer(toks, many = True)

    return JsonResponse(serializer.data, safe=False)


#retrieve, update, or delete a tok
@csrf_exempt
@app.get("/toks/{id}/")
def tok_detail(request, id):
    try:
        tok = Toks.objects.get(id=id)
    except Toks.DoesNotExist:
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
