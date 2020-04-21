from Django.contrib import admin
from Django.urls import path
#������ͼ��
from app01.views import Type1View,Type2View,Type3View,Type4View
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/type1/',Type1View.as_view()),
    path('api/type2/',Type2View.as_view()),
    path('api/type3/',Type3View.as_view()),
    path('api/type4/',Type4View.as_view())
]
