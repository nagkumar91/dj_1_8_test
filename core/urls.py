from django.conf.urls import url

from .views import list_all_TempData

urlpatterns = [
    url(r'^', list_all_TempData, name="home")
]