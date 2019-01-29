from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from django.views.decorators.csrf import csrf_exempt

#router = routers.DefaultRouter()
#router.register(r'', views.ItemsViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'^add/$', views.ItemsViewSet)

user_list = views.UserItemsViewSet.as_view({'get':'list'})
user_items_add_details = views.UserItemAddDetails.as_view()
user_items_add_photo = views.UserItemAddPhoto.as_view()
user_items_add_template = views.index

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'', user_list, name='user-list'),
    url('add_template', user_items_add_template, name='items-add-template'),
    url('add/photo', user_items_add_photo, name='items-add'),
    url('add/details', user_items_add_details, name='items-add'),
    url('', views.index),
    url(r'^(?P<user_id>[0-9a-f-]+)', views.index),
    #path('getbyempid/<int:emp_id>/<uuid:factory_id>', views.empdetails)
]

