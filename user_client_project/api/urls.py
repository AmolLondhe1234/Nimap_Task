from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('home.urls'))
    # path('products/',ProductView.as_view()),
    # path('demo/',DemoView.as_view())
    path('client/',clientlist.as_view()),
    path('client/<int:pk>/',clientup.as_view(),name='updelp'),
    path('client/<int:pk>/project/',projectlist.as_view()),
]