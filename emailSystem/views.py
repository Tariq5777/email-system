from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from emailSystem.models import Mail
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'emailSystem/index.html', {
        "user":settings.EMAIL_HOST_USER
    })

@csrf_exempt
def sendMail(request):
    if(request.method == "POST"):
        rEmail = request.POST["recipientEmail"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        newMail = Mail(rEmail = rEmail, subject=subject, message=message)
        newMail.save()
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [rEmail]
        try:
            send_mail(subject, message, email_from, recipient_list)
            return HttpResponseRedirect(reverse("success"))
        except:
            print("Error Sending Email")
            return HttpResponseRedirect(reverse("failure"))
    else: return HttpResponseRedirect(reverse("failure"))

def success(request):
    return render(request, 'emailSystem/success.html',status=200 )

def failure(request):
    return render(request, 'emailSystem/failure.html',status=200 )
    
    