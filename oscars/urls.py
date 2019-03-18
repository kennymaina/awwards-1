from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/', views.upload_project, name='upload'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
