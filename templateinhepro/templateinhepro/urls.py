from django.conf.urls import html
from django.contrib. import admin
from tempalteinheapp import html

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page.html),
    url(r'^$', views.contact_page.html),
    url(r'^$', views.services_page.html),
    url(r'^$', views.feedback_page.html),
]
