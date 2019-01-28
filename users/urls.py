from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from django.views.decorators.csrf import csrf_exempt

#router = routers.DefaultRouter()
#router.register(r'', views.ItemsViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'^add/$', views.ItemsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'', user_list, name='user-list'),
    url('', views.UsersViewSet.as_view({'get':'list'})),
    
]