class IndexView(APIView):
    """
    ��ʾ��ͼ
    """
    def get(self,request):
        j=0
        for i in request.META:
            print(i,":",request.META[i])
            j+=1
        print("��",j,"����Ϣ")
        return render(request,'index.html')
