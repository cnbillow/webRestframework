from rest_framework import serializers #�������л�ģ��
from .models import Type1,Type2,Type3,Type4 #�����������ݱ���
class Type1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type1
        fields="__all__"
class Type2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type2
        fields="__all__"
class Type3ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type3
        fields="__all__"
class Type4ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type4
        fields="__all__"
