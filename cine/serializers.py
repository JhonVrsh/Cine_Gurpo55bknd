from rest_framework import serializers
from cine.models import *


class Usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user = Usuario(
            nombre=validated_data['nombre'],
            username=validated_data['username'],
            correo=validated_data['correo'],
            telefono=validated_data['telefono'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class Cine_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cine
        fields = '__all__'


class Sala_serializer(serializers.ModelSerializer):
    cine = Cine_serializer(read_only=True)
    cine_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cine.objects.all(), source='cine')

    class Meta:
        model = Sala
        fields = '__all__'


class Cliente_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class Pelicula_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'


class Funcion_serializer(serializers.ModelSerializer):
    pelicula = Pelicula_serializer(read_only=True)
    sala = Sala_serializer(read_only=True)
    pelicula_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Pelicula.objects.all(),
                                                     source='pelicula')
    sala_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')

    class Meta:
        model = Funcion
        fields = '__all__'


class Boleta_serializer(serializers.ModelSerializer):
    cliente = Cliente_serializer(read_only=True)
    funcion = Funcion_serializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cliente.objects.all(), source='cliente')
    funcion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Funcion.objects.all(), source='funcion')

    class Meta:
        model = Boleta
        fields = '__all__'
