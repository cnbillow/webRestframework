from django.shortcuts import render
from .models import TuWen #����ͼ�ı�
from .serializers import TuWenModelSerializer#����ͼ�ı�����л���
#����drf�Ĺ������
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
# Create your views here.
class GetTuWenView(APIView):
    """
    ��ȡͼ���б�
    """
    renderer_classes = [JSONRenderer]  # ��Ⱦ��
    def get(self,request):
        t_list=TuWen.objects.all()
        re=TuWenModelSerializer(t_list,many=True)
        return Response(re.data)
