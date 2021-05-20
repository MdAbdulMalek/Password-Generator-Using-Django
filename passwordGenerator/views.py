from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import string
import random
import subprocess 
import clipboard

# Create your views here.

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "index.html")

def copy(request, ena):
    data1 = ena
    print(data1)
    clipboard.copy(data1)
    messages.success(request, " Your password coppied successfully")
    return render(request, "result2.html")

def gen(request):

    if request.method == "POST":
        len = request.POST.get('length')

        upper = request.POST.get('uppercase', 'off')
        lower = request.POST.get('lowerercase', 'off')
        punc = request.POST.get('Punctions', 'off')
        digit = request.POST.get('digit', 'off')
        plen = len
        count = 0
        final = []

        if upper == "on":
            
            sU = string.ascii_uppercase
            #sU = list(su)
            #sU = random.shuffle(sU)
            result1 = []
            result1.extend(list(sU))
            random.shuffle(result1)
            result = ("".join(result1[0:1]))
            final = result
            count = count + 1

        if lower == "on":
            sL = string.ascii_lowercase
            result2 = []
            result2.extend(list(sL))
            random.shuffle(result2)
            result = ("".join(result2[0:1]))
            if final == []:
                 final = result
            else:
                final = final + result
            #final.extend(list(result))
            count = count + 1

        if punc == "on":
            sP = string.punctuation
            result3 = []
            result3.extend(list(sP))
            random.shuffle(result3)
            result = ("".join(result3[0:1]))
            if final == []:
                 final = result
            else:
                final = final + result
            count = count + 1

        if digit == "on":
            sD = string.digits
            result4 = []
            result4.extend(list(sD))
            random.shuffle(result4)
            result = ("".join(result4[0:1]))
            if final == []:
                 final = result
            else:
                final = final + result
            count = count + 1

        sonkha = int(plen) - count

        #listToStr = ' '.join(map(str, s))

        while count >= 1:
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            random.shuffle(s)
            #p = ("".join(random.sample(s, plen)))
            p = ("".join(s[0:int(sonkha)]))
            lol = final + p
            params = {'purpose': 'Generated Password', 'ana': lol}

            return render(request, "result.html", params)
        else:
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            random.shuffle(s)

            #p = ("".join(random.sample(s, plen)))
            p = ("".join(s[0:int(plen)]))
            data1 = p

            #print(p)
            params = {'purpose': 'Generated Password', 'ana': p}

            return render(request, "result.html", params)


    return render(request, "index.html")
