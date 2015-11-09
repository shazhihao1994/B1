from django.conf.urls.defaults import patterns, include, url
from myweb.BookDB import views



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^search/noselect/$', views.search_form),
    (r'^search/authorandbook/$', views.fTitle),
    (r'^search/delete/$', views.fDelete),
    (r'^search/$', views.search),
    (r'^search_form/$', views.search_form),
    (r'^$', views.search_form),
    (r'^search/search_form/$', views.search_form),
    (r'^search/authorandbook/search_form/$', views.search_form),
    (r'^search/Add/$', views.Add_form),
    (r'^Add_result/$', views.Add),
    (r'Add_result/search_form/',views.search_form),
    (r'^search/update_form/$', views.update_form),
    (r'^update/$', views.update),
    (r'^update/search_form/$',views.search_form),
                      
                
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^myweb/', include('myweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
)
