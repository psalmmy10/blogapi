from rest_framework import serializers
from .models import blogs, category

class blogserializer (serializers.ModelSerializer):
    class meta :
        model = blogs
        fields = '__all__'

class categoryserializer (serializers.ModelSerializer):
    class meta :
        model = category
        fields = '__all__'