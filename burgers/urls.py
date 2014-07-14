from django.conf.urls import patterns, include, url

from django.contrib import admin

from client import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'burgers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index),
    url(r'^order/(\d*)/?$', views.order),
    url(r'^order_list$', views.order_list),
    url(r'^orders$', views.orders),
    url(r'^ingredients$', views.ingredients),
    url(r'^ingredients_list$', views.ingredients_list),
    url(r'^logout$', views.logout_view),
    url(r'^login$', views.login_view),

    
)
