class ShopView(LoginRequiredMixin,View):
    """
    ������ͼ
    """
    def get(self,request):
        return render(request,'shop.html',{'user':request.user})
    def post(self,request):
        return HttpResponse('200')
