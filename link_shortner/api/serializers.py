from random import choices
from string import ascii_letters, digits

from rest_framework.serializers import ModelSerializer

from .models import ShortLink


class ShortLinkSerializer(ModelSerializer):
    
    class Meta:
        model = ShortLink
        fields = '__all__'
        
    def create(self, validated_data):
        token = ''.join(choices(ascii_letters + digits, k=6))
        return ShortLink.objects.create(token=token, **validated_data)