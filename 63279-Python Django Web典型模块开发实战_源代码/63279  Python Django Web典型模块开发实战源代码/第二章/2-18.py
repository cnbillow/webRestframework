from .serializers import BookModelSerializer
from rest_framework.response import Response
from .models import UserProfile,Book
from rest_framework import mixins
from rest_framework import generics
class BookMixinView2(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get(self,request,*args,**kwargs):
        APIKey = self.request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            balance=developer.money
            if balance>0:
                isbn = self.request.query_params.get("isbn", 0)
                developer.money -= 1
                developer.save()
                self.queryset = Book.objects.filter(isbn=int(isbn))
                return self.list(request, *args, **kwargs)
            else:
                return Response("�ֵܣ��ֵ�����Ҫ��Ǯ��ʱ�򣡺ÿ��İ���")
        else:
            return Response("���޴��˰�")
