from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name="profile_detail"),
    path('my_profile_update/', views.edit_profile, name='my_profile_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
