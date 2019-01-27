from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from django.views.decorators.csrf import csrf_exempt

#router = routers.DefaultRouter()
#router.register(r'', views.ItemsViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'^add/$', views.ItemsViewSet)

user_list = views.ItemsViewSet.as_view({'get':'list'})
items_add = views.ItemsAddViewSet.as_view()
items_add_template = views.index

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'', user_list, name='user-list'),
    url('add_template', items_add_template, name='items-add-template'),
    url('add', csrf_exempt(items_add), name='items-add'),
    url('', user_list),
    
]