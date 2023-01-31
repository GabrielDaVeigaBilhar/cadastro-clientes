from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse

from CadastroClientes.models import Cliente
from CadastroClientes.serializers import ClienteSerializer

@csrf_exempt
def clienteApi(request,id=0):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(cliente, many=True)  
        return JsonResponse(cliente_serializer.data, safe=False)
    elif request.method == 'POST':
        cliente_data=JSONParser().parse(request)
        cliente_serializer = ClienteSerializer(data=cliente_data)
        if cliente_serializer.save():
            return JsonResponse("Cadastrado com sucesso", safe=False)
        return JsonResponse("Não cadastrou", safe=False)
    elif request.method == 'PUT':
        cliente_data = JSONParser().parse(request)
        cliente = Cliente.objects.get(ClienteId=cliente_data['ClienteId'])
        cliente_serializer = ClienteSerializer(cliente,data=cliente_data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Erro ao atualizar")

@csrf_exempt
def clienteConsultaId(request,id):

    if request.method == 'GET':
        cliente = cliente = Cliente.objects.get(ClienteId=id)
        cliente_serializer = ClienteSerializer(cliente) 
        return JsonResponse(cliente_serializer.data, safe=False)

@csrf_exempt
def clienteConsultaNome(request,nome):

    if request.method == 'GET':
        cliente = cliente = Cliente.objects.get(Nome=nome)
        cliente_serializer = ClienteSerializer(cliente) 
        return JsonResponse(cliente_serializer.data, safe=False)

@csrf_exempt
def clienteConsultaCPF(request,cpf):

    if request.method == 'GET':
        cliente = cliente = Cliente.objects.get(CPF=cpf)
        cliente_serializer = ClienteSerializer(cliente) 
        return JsonResponse(cliente_serializer.data, safe=False)


