from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import time
from django.utils.translation import ugettext
from django.views.decorators import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    t = time.localtime()
    n = t[6]
    weekdays = [
        ugettext('Monday'),
        ugettext('Tuesday'),
        ugettext('Wednesday'),
        ugettext('Thursday'),
        ugettext('Friday'),
        ugettext('Saturday'),
        ugettext('Sunday')
    ]
    responseContext = {
        'lang': request.LANGUAGE_CODE,
        'weekday': weekdays[n]
    }
    response = render_to_response('i18n.html',
                                  responseContext,
                                  context_instance=RequestContext(request))
    return response
