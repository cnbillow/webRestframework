from .serializers import BookModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile,Book
class BookAPIView2(APIView):
    """
    ʹ��ModelSerializer
    """
    def get(self, request, format=None):
        APIKey=self.request.query_params.get("apikey", 0)
        developer=UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            balance=developer.money
            if balance>0:
                isbn = self.request.query_params.get("isbn", 0)
                books = Book.objects.filter(isbn=int(isbn))
                books_serializer = BookModelSerializer(books, many=True)
                developer.money-=1
                developer.save()
                return Response(books_serializer.data)
            else:
                return Response("�ֵܣ��ֵ�����Ҫ��Ǯ��ʱ�򣡺ÿ��İ���")
        else:
            return Response("���޴��˰�")
