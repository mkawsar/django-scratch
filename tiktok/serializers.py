from .models import TiktTokVideo
from rest_framework import serializers


class TikTokVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TiktTokVideo
        fields = '__all__'
