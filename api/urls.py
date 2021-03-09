from .views import ImageViewSet, LeadViewSet, SearchPost
from rest_framework import routers
from django.urls import path, include

app_name	=  'api-images'

router = routers.DefaultRouter()
router.register(r'images', ImageViewSet, 'images')
router.register(r'leads', LeadViewSet, 'leads' )
router.register(r'SearchPost', SearchPost, 'searchImage')



urlpatterns =[
		path('', include(router.urls)),

]