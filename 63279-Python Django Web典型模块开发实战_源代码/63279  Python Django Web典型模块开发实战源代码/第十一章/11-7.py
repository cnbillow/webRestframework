from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
class GetBookView(View):
    """
    ��ȡ����ͼ��
    """
    @method_decorator(cache_page(3))
    def get(self,request,id):
        book=Books.objects.filter(id=id).first()
        print(book.pv)
        book.pv+=1
        book.save()
        return render(request,'book.html',{'t':book})
