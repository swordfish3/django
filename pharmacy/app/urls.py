from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = (
        url(r'^$', views.index, name='index'),
        url(r'^allproducts/$', login_required(views.all_products), ),
        # url(r'^id/$', login_required(views.searchByID), name='id'),

)