from rest_framework import serializers
from CadastroClientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('ClienteId', 'Nome', 'CPF', 'Telefone', 'Sexo', 'CEP', 'Cidade', 'Estado', 'Logradouro')