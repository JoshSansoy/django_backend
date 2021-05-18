from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'monsters', views.MonsterView, 'monster')

urlpatterns = [
    path('', include(router.urls)),
    path('fight/', views.FighterSelectView.as_view())
]