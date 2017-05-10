from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = (
        url(r'^$', views.index, name='index'),
        url(r'^allproducts/$', login_required(views.all_products), ),
        url(r'^allproducts/$', login_required(views.get_cart), ),
        url(r'^allproducts/(?P<pharmacyid>\d+)/$', login_required(views.product_info), ),
        url(r'^allproducts/(?P<pharmacyid>\d+)/$', login_required(views.post_form), ),
        url(r'^allproducts/(?P<pharmacyid>\d+)/add/$', login_required(views.add_to_cart), ),
        url(r'^allproducts/(?P<name>\d+)/remove/$', login_required(views.remove_from_cart), ),
        url(r'', login_required(views.get_cart), ),

)