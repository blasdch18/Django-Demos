from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """api view de prueba"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format= None):
        """retornar lista  de caracteristicas del APIView"""

        an_apiview = [
            'usamos metodos HTTP como funciones (get, post, patch, put, delete',
            'es similar a una vista tradicional de Django',
            'nos da el mayor control sobre la logica de nuestra aplicacion',
            'esta mapeado manualmente a los URLS',
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post (self,request):
        """crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put (self ,request):
        """ maneja actualizar un objeto"""
        return Response({'method': 'PUT'})

    def patch (self ,request, pk=None):
        """maneja actualizacion parcial de un objeto"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request ,pk=None):
        """"delete un objeto"""
        return Response({'method': 'DELETE'})

