from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'courses'

routers = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('subjects/',
        views.SubjectListView.as_view(),
        name='Subject_list'),
    path('subjects/<pk>/',
        views.SubjectDetailView.as_view(), 
        name='subject_detail'),
    path('', include(router.urls)),
]