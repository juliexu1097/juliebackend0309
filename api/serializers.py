from images.models import Image, Lead
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields ='__all__'

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields ='__all__'





