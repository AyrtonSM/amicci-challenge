from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, viewsets
from .models import *
from .serializers import *
import logging as logger


class CategoryViewSet(viewsets.ViewSet):
    default_categories = ['Novo Produto', 'Troca de Fornecedor', 'Reformulação de Produto']

    for category in default_categories:
        try:
            retrieved_category = Category.objects.get(name=category)
            if category == retrieved_category.name:
                continue

        except:
            Category.objects.create(name=category)

    def list(self, request):
        """ Retrieve all categories """

        queryset = Category.objects.all()
        serializer_class = CategorySerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        """ Retrieve a category by the id """

        item = Category.objects.get(pk=pk)
        serializer_class = CategorySerializer(item, many=False)
        return Response(serializer_class.data)

    def create(self, request):
        """ Given the request data, this method create a new category """

        if 'name' not in request.data:
            return Response('Erro inesperado', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        name = request.data['name']
        category = Category.objects.create(name=name)

        serialized_category = CategorySerializer(category, many=False)

        return Response(serialized_category.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """ Given the request data and the id, update the category """

        if 'name' not in request.data or pk is None:
            return Response("Erro inesperado", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            item = Category.objects.get(pk=request.data['id'])
        except:
            logger.warning("The required Category was not found, creating a new resource")
            return Response('Objeto Categoria inválido.', status=status.HTTP_400_BAD_REQUEST)

        item.name = request.data['name']

        try:
            item.save()
            return Response(CategorySerializer(item, many=False).data, status=status.HTTP_200_OK)
        except:
            return Response('Objeto Categoria inválido.', status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass


class VendorViewSet(viewsets.ViewSet):
    def list(self, request):
        """ Retrieve all categories """

        queryset = Vendor.objects.all()
        serializer_class = VendorSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        """ Retrieve a vendor by the id """

        item = Vendor.objects.get(pk=pk)
        serializer_class = VendorSerializer(item, many=False)
        return Response(serializer_class.data)

    def create(self, request):
        """ Given the request data, this method create a new vendor """

        if 'name' not in request.data:
            return Response('Erro inesperado', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        name = request.data['name']
        vendor = Vendor.objects.create(name=name)

        serialized_vendor = VendorSerializer(vendor, many=False)

        return Response(serialized_vendor.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """ Given the request data and the id, update the vendor """

        if 'name' not in request.data or pk is None:
            return Response("Erro inesperado", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            item = Vendor.objects.get(pk=request.data['id'])
        except:
            return Response('Não há fornecedor disponível', status=status.HTTP_404_NOT_FOUND)

        item.name = request.data['name']

        try:
            item.save()
            return Response(VendorSerializer(item, many=False).data, status=status.HTTP_200_OK)
        except:
            return Response('Requisição inválida', status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass
