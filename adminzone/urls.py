from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'adminzone'

urlpatterns = [
    re_path(r'^$', views.index, name = 'admin_index'),
    re_path(r'^treatment', views.treatment, name = 'admin_treatment'),
    re_path(r'^about', views.about, name = 'admin_about'),
    re_path(r'^project', views.project, name = 'admin_project'),
    re_path(r'^signout', views.signout, name = 'admin_signout'),
    re_path(r'^predict', views.predict, name = 'predict')
]