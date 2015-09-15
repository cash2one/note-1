from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse, Http404
from django.views.defaults import bad_request
from django.core.mail import send_mail


def index(request):
    return render(request, 'test.html')


def ajax_list(request):
    a = int(request.GET.get('a', '1'))
    b = request.GET.get('b', '')
    print b
    a = range(a)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


@csrf_exempt
def ajax_add(request):
    a = int(request.POST.get('a', 0))
    b = int(request.POST.get('b', 0))
    ret = a + b
    ret = {'ret':ret}
    return JsonResponse(ret)


from django.core.mail import EmailMessage

def send_html_mail(subject, html_content, recipient_list):
    msg = EmailMessage(subject, html_content, 'crmtest@100credit.com', recipient_list)
    msg.content_subtype = "html" # Main content is now text/html
    msg.send(fail_silently=False)


@csrf_exempt
def sendmail(request):
    subject = request.POST.get('subject')
    content = request.POST.get('content')
    print subject
    print content
    try:
        send_html_mail(subject, '<h1>CRM!TEST</h1>', ["xue.bai@100credit.com"])
        # send_mail(subject, content, 'crmtest@100credit.com', ["xue.bai@100credit.com"], fail_silently=False)
    except Exception, e:
        return JsonResponse({'msg': unicode(e)})
    return JsonResponse({'msg': 'success!'})


def testurl(request):
    return JsonResponse(dict(request.GET.items()))