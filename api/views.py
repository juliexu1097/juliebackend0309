from rest_framework import viewsets, permissions
from api.serializers import ImageSerializer, LeadSerializer
from images.models import Image, User
from django.db.models import Q
from django.views.generic import ListView


class ImageViewSet(viewsets.ModelViewSet):
    # queryset = Image.objects.all().order_by('-uploaded')
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImageSerializer

    def get_queryset(self):

        return  self.request.user.image.all().order_by('-uploaded')

    def perform_create(self, serializer):
        serializer.save(imageOwner=self.request.user)


class LeadViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LeadSerializer

    #Get the users that have been created from that user
    def get_queryset(self):
       return self.request.user.leads.all()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SearchPost(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ImageSerializer
    paginate_by = 100
    def get_queryset(self):
        print(self)
        print("Query: ----------" )
        # Get the value from the
        query = self.request.GET.get('q')
        print(query)
        return self.request.user.image.filter(
            Q(classField__icontains=query) |
            Q(picture__icontains=query)|
            Q(uploaded__icontains=query)
        ).distinct()
