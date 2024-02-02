from django.urls import path
from . import views 

# this is used when calling for certain url
# ({app_name}:{path_name})
# exp("application:index") 
app_name="stage"


urlpatterns=[
    path('',views.index, name='index'),
    path('<str:id_evenement>/',views.show, name='show')
]
