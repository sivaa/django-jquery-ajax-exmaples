from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from urllib import urlopen #@UnresolvedImport
import html, time

def home(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def javascript(request):
    return render_to_response('javascript.html', locals(), context_instance=RequestContext(request))

def load_basic(request):
    return render_to_response('load_basic.html', locals(), context_instance=RequestContext(request))

def load_basic_dom(request):
    return render_to_response('load_basic_dom.html', locals(), context_instance=RequestContext(request))

def load_get(request):
    return render_to_response('load_get.html', locals(), context_instance=RequestContext(request))

def load_post(request):
    return render_to_response('load_post.html', locals(), context_instance=RequestContext(request))

def load_callback(request):
    return render_to_response('load_callback.html', locals(), context_instance=RequestContext(request))

def json(request):
    return render_to_response('json.html', locals(), context_instance=RequestContext(request))

def script(request):
    return render_to_response('script.html', locals(), context_instance=RequestContext(request))

def get(request):
    return render_to_response('get.html', locals(), context_instance=RequestContext(request))

def post(request):
    return render_to_response('post.html', locals(), context_instance=RequestContext(request))

def advanced(request):
    return render_to_response('advanced.html', locals(), context_instance=RequestContext(request))

def advanced_handlers(request):
    return render_to_response('advanced_handlers.html', locals(), context_instance=RequestContext(request))


def ajax_load_basic(request):
    time.sleep(2)
    if not request.is_ajax():
        HttpResponse (" Not an AJAX request ")
    return HttpResponse(html.HTML_TEXT);

def ajax_load_get(request):
    time.sleep(2)
    if not request.is_ajax():
        HttpResponse (" Not an AJAX request ")
    if request.method == 'GET':
        if request.GET['company'] == 'google':
            return HttpResponse(html.HTML_TEXT_GOOGLE);
        if request.GET['company'] == 'yahoo':
            return HttpResponse(html.HTML_TEXT_YAHOO);
        return HttpResponse(html.HTML_TEXT);
       
    return HttpResponse (" Not an GET request ")

@csrf_exempt
def ajax_load_post(request):
    time.sleep(2)
    if not request.is_ajax():
        HttpResponse (" Not an AJAX request ")
    if request.method == 'POST':
        if request.POST['company'] == 'google':
            return HttpResponse(html.HTML_TEXT_GOOGLE);
        if request.POST['company'] == 'yahoo':
            return HttpResponse(html.HTML_TEXT_YAHOO);
        return HttpResponse(html.HTML_TEXT);
       
    return HttpResponse (" Not an POST request ")


def ajax_json(request):
    time.sleep(2)
    if not request.is_ajax():
        HttpResponse (" Not an AJAX request ")        
    json_text =  urlopen("http://money.rediff.com/money1/currentstatus.php?companycode=" + request.REQUEST['company'] ).read()
    #print json_text        
    return HttpResponse (json_text)

def ajax_script(request):
    time.sleep(2)
    if not request.is_ajax():
        HttpResponse (" Not an AJAX request ")       
    script = """
          alert("The page will be redirected to MSN after 5 seconds");
          setInterval(function(){window.location = "http://www.msn.com/"},5000);
      """
    return HttpResponse (script)


def ajax_get(request):
    time.sleep(2)
    if not request.is_ajax():
        HttpResponse (" Not an AJAX request ")
    if request.method == 'GET':
        if request.GET['company'] == 'google':
            return HttpResponse(html.HTML_TEXT_GOOGLE);
        if request.GET['company'] == 'yahoo':
            return HttpResponse(html.HTML_TEXT_YAHOO);
        return HttpResponse(html.HTML_TEXT);
       
    return HttpResponse (" Not an GET request ")

@csrf_exempt
def ajax_post(request):
    time.sleep(2)
    if not request.is_ajax():
        HttpResponse (" Not an AJAX request ")
    if request.method == 'POST':
        if request.POST['company'] == 'google':
            return HttpResponse(html.HTML_TEXT_GOOGLE);
        if request.POST['company'] == 'yahoo':
            return HttpResponse(html.HTML_TEXT_YAHOO);
        return HttpResponse(html.HTML_TEXT);
       
    return HttpResponse (" Not an POST request ")


def ajax_error(request):
    time.sleep(2)
    return " Not an POST request "

def ajax_sync(request):
    time.sleep(7)
    return HttpResponse(html.HTML_TEXT)
