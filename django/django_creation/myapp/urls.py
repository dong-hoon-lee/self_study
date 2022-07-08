from django.urls import path
from myapp import views

urlpatterns = [
    # 아무런 path 없이(즉, 메인화면) 접속하면 views파일 안의 index 함수를 실행하도록 함
    path('', views.index),

    # create path로 접속했을 때 화면 보여줌
    path('create/', views.create),

    # < >: 안에 들어가는 값을 가변변수로 받아옴
    path('read/<id>/', views.read)
]
