from rest_framework import serializers
#�������±���û���
from .models import UserProfile,Article
class UserProfileSerializer(serializers.ModelSerializer):
	������
	���л��û���
	������
    class Meta:
        model=UserProfile
        fields = "__all__"
class ArticleSerializer(serializers.ModelSerializer):
	������
	���л�������
	������
    class Meta:
        model=Article
        fields = "__all__"
