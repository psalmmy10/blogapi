from django.urls import path,include
from .views import blogsViewset, categoryViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('blogs',blogsViewset, basename='blogs')
router.register('category',categoryViewset, basename='category')


urlpatterns =[
    path('',include(router.urls))
]