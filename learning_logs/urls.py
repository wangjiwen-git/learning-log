"""定义learning_logs的URL模式"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 其他页面的URL模式
    path('topics/', views.topics, name='topics'),

    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]