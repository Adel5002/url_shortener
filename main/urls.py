from django.urls import path


from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('shorten', shorten_post, name='shorten_post'),
    path('shorten/<str:url>', shorten, name='shorten'),
    path('<str:url_hash>', redirect_hash, name='redirect'),

]