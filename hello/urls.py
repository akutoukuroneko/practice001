#django4でテキストと変更あり
from django.urls import path
from .views import HelloView

#django4でテキストと変更あり
urlpatterns = [
    path(r'', HelloView.as_view(), name='index'),
]