from django.urls import path
from worldcup import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'worldcup'

urlpatterns = [
    path('', views.worldcup_view, name='worldcup_view'),
    path('start/<int:contest_id>/', views.start, name='start'),
    #path('ajax_view/<int:contest_id>/', views.ajax_view, name='ajax_view'),
   # path('ajax_view/', views.ajax_view, name='ajax_view'),
    path('makecontest/', views.make_contest, name='make_contest'),
    path('middle/', views.middle, name='middle'),
    path('make/<int:contest_id>/', views.make_worldcup , name='make_worldcup'),
    path('uploadfile/<int:contest_id>/',views.upload_file, name='upload_file'),
    path('result/', views.make_quit, name='make_quit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
