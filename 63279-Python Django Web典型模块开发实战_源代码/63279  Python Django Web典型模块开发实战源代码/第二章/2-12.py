from rest_framework import serializers
from .models import UserProfile,Book
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields="__all__"#��������������ֶζ����л�
