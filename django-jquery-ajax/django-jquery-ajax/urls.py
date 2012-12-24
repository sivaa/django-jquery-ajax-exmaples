from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()


urlpatterns += patterns('',
    
    (r'^ajax/load_basic',   'myapp.views.ajax_load_basic'),
    (r'^ajax/load_get',     'myapp.views.ajax_load_get'),
    (r'^ajax/load_post',    'myapp.views.ajax_load_post'),
    (r'^ajax/json',         'myapp.views.ajax_json'),
    (r'^ajax/script',       'myapp.views.ajax_script'),
    (r'^ajax/get',          'myapp.views.ajax_get'),
    (r'^ajax/post',         'myapp.views.ajax_post'),
    (r'^ajax/error',        'myapp.views.ajax_error'),
    (r'^ajax/sync',         'myapp.views.ajax_sync'),

    (r'^javascript',        'myapp.views.javascript'),
    (r'^load_basic_dom',    'myapp.views.load_basic_dom'),
    (r'^load_basic',        'myapp.views.load_basic'),
    (r'^load_get',          'myapp.views.load_get'),
    (r'^load_post',         'myapp.views.load_post'),
    (r'^load_callback',     'myapp.views.load_callback'),
    (r'^json',              'myapp.views.json'),
    (r'^script',            'myapp.views.script'),
    (r'^get',               'myapp.views.get'),
    (r'^post',              'myapp.views.post'),
    (r'^advanced_handlers', 'myapp.views.advanced_handlers'),
    (r'^advanced',          'myapp.views.advanced'),
    
    (r'^editor',          'myapp.views.editor'),    
    (r'^ckeditor/', include('ckeditor.urls')),

    
    (r'', 'myapp.views.home'),
)



