import datetime

from rest_framework import viewsets
from cine.serializers import *
from cine.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class Usuario_view(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_serializer


class Cine_view(viewsets.ModelViewSet):
    queryset = Cine.objects.all()
    serializer_class = Cine_serializer


class Sala_view(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = Sala_serializer


class Cliente_view(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Cliente_serializer


class Pelicula_view(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = Pelicula_serializer


class Funcion_view(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = Funcion_serializer


class Boleta_view(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = Boleta_serializer


# otras consultas
# Cliente.objects.filter(nombre__contains=dato)
# 1 Boleta.objects.filter(funcion__pelicula__nombre__contains=dato)
# 2 Boleta.objects.filter(funcion__boleta__valor__gt=dato)
# 3 Boleta.objects.filter(funcion__boleta__asientos__range=(dato, dato2))
# 4 Boleta.objects.filter(funcion__fecha=dato)
# 5 Boleta.objects.filter(funcion__fecha__range=(dato, dato2))
# 6 TODO realizar modificación a la tabla de clientes para almacenar la edad
class Prueba_view(viewsets.ModelViewSet):
    def get_queryset(self):
        dato = self.request.query_params.get('dato')
        dato2 = self.request.query_params.get('dato2')
        if dato:
            return Boleta.objects.filter(funcion__fecha__range=(dato, dato2))
        else:
            return Boleta.objects.all()

    serializer_class = Boleta_serializer


class TokenProvider(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = Usuario_serializer(user)
        return Response(usuario.data)
