from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
class IndexView(APIView):
    """
    ��ʾ��ͼ
    """
    def get(self,request):
        return render(request,'index.html')
