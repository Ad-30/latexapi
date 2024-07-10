from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()



urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
    path('latexResume',LaTeXToPDFView.as_view(),name='latexResume'),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
]
