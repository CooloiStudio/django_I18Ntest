from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import time
from django.utils.translation import ugettext
from django.views.decorators import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext


def weekday():
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
    return weekdays[n]


def home(request):
    content = {
        'lang': request.LANGUAGE_CODE,
        'weekday': weekday()
    }
    response = render_to_response('i18n.html',
                                  content,
                                  context_instance=RequestContext(request))
    return response


def fake_select(request):
    content = {
        'lang': request.LANGUAGE_CODE,
        'weekday': weekday()
    }
    response = render_to_response('FakeSelect.html',
                                  content,
                                  context_instance=RequestContext(request))
    return response
