from rest_framework import serializers
#�������ݱ���
from .models import CommonVideo,VIPVideo,SVIPVideo
#���������ݱ���������л� 
class CommonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommonVideo
        fields = "__all__"
class VIPVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=VIPVideo
        fields = "__all__"
class SVIPVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SVIPVideo
        fields = "__all__"
