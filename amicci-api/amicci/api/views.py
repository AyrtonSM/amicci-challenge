from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .models import *
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @api_view(['GET', 'POST'])
    def get_all_categories(request):
        if request.method == 'POST':
            return Response({"message": "Got some data!", "data": request.data})
        return Response({"message": "Hello, world!"})

        #     if request.method != 'GET':
        #         return HttpResponse('Erro inesperado')
        #
        #     data = [{
        #         'id': 1,
        #         'name': 'Novo Produto',
        #     },
        #         {
        #             'id': 2,
        #             'name': 'Troca de Fornecedor',
        #         },
        #         {
        #             'id': 3,
        #             'name': 'Reformulação de Produto',
        #         }]
        #
        #     return JsonResponse({'content-response': data})
