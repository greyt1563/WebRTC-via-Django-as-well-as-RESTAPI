from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from webapp.models import ContactModel
from django.contrib import messages
from django.http import JsonResponse
import string
import random
import base64


# Create your views here.
def index(request):
    return render(request, "index.html")

@csrf_exempt
def ui(request):
    if request.is_ajax and request.method == "POST":
        nick_name = request.POST.get("fname", None).split(",")[1]
        z=nick_name.replace(" ","+")
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        y = base64.b64decode(z)
        fi = open("./testfileupload/"+x+".jpg", "wb")
        fi.write(y)
        fi.close()
        return JsonResponse({"valid":True}, status = 200)
    else:
        return JsonResponse({}, status = 400)


def error_404_view(request, exception):
    t4 = loader.get_template('custom404.html')
    return HttpResponse(t4.render())
