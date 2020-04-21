from django.shortcuts import render
#����APIview
from rest_framework.views import APIView
#�����û����ݱ���
from .models import UserProfile,Article
#�������л���
from .serializers import UserProfileSerializer,ArticleSerializer
#����drf����ģ��
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
#����Qģ��
from django.db.models import Q
# Create your views here.
class GetArticleViews(APIView):
    """
    ��ȡ�����б�
    """
    def get(self,request):
        keyword=request._request.GET.get('keyword')
        # print(keyword)
        if keyword:
            article_list = Article.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword))
        else:
            article_list = Article.objects.all()
        re = ArticleSerializer(article_list, many=True)
        return Response(re.data)
