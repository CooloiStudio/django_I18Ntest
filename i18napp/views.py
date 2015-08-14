from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import time
from django.utils.translation import ugettext
from django.views.decorators import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    t  = time.localtime()
    n  = t[6]
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    return HttpResponse('Today is:'+weekdays[n])

def trans_home(request):
    t  = time.localtime()
    n  = t[6]
    weekdays = [ugettext('Monday'),ugettext('Tuesday'),ugettext('Wednesday'),ugettext('Thursday'),
                        ugettext('Friday'),ugettext('Saturday'),ugettext('Sunday')]
    return HttpResponse('Today is:'+weekdays[n])

def trans_template(request):
    language=request.POST.get('language','zh-CN')
    responseContext={}
    responseContext['lang'] = request.LANGUAGE_CODE
    resp = render_to_response('i18n.html', responseContext,
                                context_instance=RequestContext(request))
    return resp