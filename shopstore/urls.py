from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^accounts/logout/$',views.logout_view),url(r'^accounts/login/$',views.login_view),
    url(r'^accounts/dashboard/$',views.dashboard),url(r'^item/details/(?P<item_id>[0-9]+)/$',views.itemdetails),
    url(r'^search/$',views.search),url(r'^$',views.index),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)