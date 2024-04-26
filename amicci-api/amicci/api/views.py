from rest_framework.response import Response
from rest_framework import permissions, viewsets
from .models import *
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        item = Category.objects.get(pk=pk)
        serializer_class = CategorySerializer(item, many=False)
        return Response(serializer_class.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass



