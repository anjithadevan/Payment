from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('payment/<int:id>/', TemplateView.as_view(template_name="base.html")),
    path('payments', PaymentViewSet.as_view()),
]