from django.shortcuts import render
from django.views.generic.base import View
from .models import Books
# Create your views here.
class BookListView(View):
    """
    ��ȡͼ���б�
    """
    def get(self,request):
        list=Books.objects.all()
        return render(request,'booklist.html',{'list':list})
class GetBookView(View):
    """
    ��ȡ����ͼ��
    """
    def get(self,request,id):
        book=Books.objects.filter(id=id).first()
        print(book.pv)
        book.pv+=1
        book.save()
        return render(request,'book.html',{'t':book})
