from rest_framework import serializers
#�����û������±����۱��ؼ��ʱ�
from .models import UserProfile,Article,Comment,Card
class UserProfileSerializer(serializers.ModelSerializer):
	������
	���л��û���
	������
    class Meta:
        model=UserProfile
        fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
	������
	���л����۱�
	������
    class Meta:
        model=Comment
        fields = "__all__"
class ArticleSerializer(serializers.ModelSerializer):
	������
	���л����±�
	������
    class Meta:
        model=Article
        fields = "__all__"
class CardSerializer(serializers.ModelSerializer):
	������
	���л�Υ���ʱ�
	������
    class Meta:
        model=Card
        fields = "__all__"
