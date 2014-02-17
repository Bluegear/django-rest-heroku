from django.core.urlresolvers import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from simplerest.api.urls import urlpatterns


@api_view(['GET'])
@permission_classes((AllowAny,))
def home(request):
    """<h2>Welcome!</h2>"""

    name = ""

    if request.user:
        name = request.user.username

    link = "http://%s%s" % (request.META['HTTP_HOST'], reverse('simplerest.api.views.api_list'))

    return Response(
        {"message": "GRRR! %s" % name, "api_list": link})

@api_view(['GET'])
def api_list(request):
    """<h3>Log in is required to view this page.</h3>
    """
    apis = []
    for url in urlpatterns:
        apis.append("http://%s%s" % (request.META['HTTP_HOST'], reverse(url._callback_str)))

    return Response({"apis": apis})
