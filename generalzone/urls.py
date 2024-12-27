from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'generalzone'

urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^treatment', views.treatment, name = 'treatment'),
    re_path(r'^about', views.about, name = 'about'),
    re_path(r'^project', views.project, name = 'project'),
    re_path(r'^login', views.login, name = 'login'),
    re_path(r'^validate', views.validate, name = 'validate'),
    re_path(r'^signup', views.signup, name = 'signup'),
    re_path(r'^createUser', views.createUser, name = 'createUser')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)