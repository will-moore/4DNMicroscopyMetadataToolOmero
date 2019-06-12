
from . import views
from django.conf.urls import url, patterns

urlpatterns = patterns(

    'django.views.generic.simple',

    url(r'^$', views.index, name='microscopyMetadataTool_index'),

    url(r'^save_microscope/$', views.save_microscope,
        name='microscopyMetadataTool_save_microscope'),
)
