from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.repositories import FreteRepository
from api.serializers import FreteSerializer

frete_repository = FreteRepository()

class FreteGetAllView(APIView):
    def get(self, request):
        fretes = frete_repository.get_all()
        serializer = FreteSerializer(fretes, many=True)

        return Response(data=serializer.data)