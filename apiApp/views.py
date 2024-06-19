from django.shortcuts import render
from .models import blogs,category
from .serilaizers import blogserializer, categoryserializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response 

class blogsViewset (viewsets.GenericViewSet, mixins.ListModelMixin , mixins.RetrieveModelMixin):
    queryset = blogs.objects.all()
    serializer_class = blogserializer
    lookup_field = 'slug'
    
class categoryViewset (viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = category.objects.all()
    serializer_class = categoryserializer
    lookup_field = 'id'
    
class categoryDetailsApiView(viewsets.ViewSet):
    def retrieve(self,request,pk=None):
        queryset = blogs.objects.filter(category=pk)
        serializers = blogserializer(queryset, many=True)
        return Response(serializers.data)
    
class PorpulrPostApiView(viewsets.ViewSet):
    def list(self,request,pk=None):
        queryset = blogs.objects.filter(postLabel__iexact ='PORPULAR').order_by('-id')[0:4]
        serializers = blogserializer(queryset, many=True)
        return Response(serializers.data)