from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token

class ItemsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


#@csrf_exempt
#class ItemsAddViewSet(viewsets.ModelViewSet):
class ItemsAddViewSet(views.APIView):
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'items_add.html'

    #@classmethod
    #def get_extra_actions(cls):
    #    return []

    queryset = User.objects.all()
    serializer_class = UserSerializer

    #@action(detail=True, methods=['get'])
    #def get_template(self):
    #    return Response({'items': 'items'})

    #@csrf_exempt
    #@method_decorator(csrf_exempt)
    #@action(detail=True, methods=['post'])
    def post(self, request, format=None):
        #serializer = self.get_serializer(data=request.data)

        print("request " + str(request.user.id))

        #user = User.objects.create(
        #    username="validated_data['username']11"
        #)
        #user.set_password("validated_data['password']")
        #user.save()

        #User.objects.create_user(
        #    serialized.init_data['email'],
        #    serialized.init_data['username'],
        #    serialized.init_data['password']
        #)

        #bffd204f6beaa5ee59927ac1d0073cc37cdd6a27

        #token = Token.objects.create(user=user)
        #print(token.key)

        return Response({'items': 'items'})
    #    return Response({'items': 'items'}, status=status.HTTP_201_CREATED)


    #queryset = User.objects.all().order_by('-date_joined')
    #serializer_class = UserSerializer



def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 'latest_question_list'}
    return render(request, 'items_add.html', context)
