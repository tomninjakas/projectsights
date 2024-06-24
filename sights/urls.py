from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sights import views
from django.conf.urls import include


urlpatterns = [
    path('sights/', views.SightsList.as_view()),
    path('sights/<int:pk>/', views.SightsDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)
