#����
from app01.views import AuthView,CommonVideoView
urlpatterns = [
    #����
    path('common/',CommonVideoView.as_view(),name='common'),
]
