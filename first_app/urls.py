



from django.urls import path
from . import views
urlpatterns = [

    path("",views.app,name='home'),
    path("about/",views.about,name='about'),
    path("details/",views.details,name = 'detail')
    
]
