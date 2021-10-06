# my  file created by me
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html', )
def analyse(request):
    textdata = request.GET.get('text', 'default')
    removepun = request.GET.get('removepunc')
    capital = request.GET.get('capital')
    charval = request.GET.get('charcount')
    if(removepun == "on"):
        analtext=""
        for i in textdata:
            if i.isalpha():
                analtext= analtext+i
        textdata=analtext
        params = {'purpose': 'Removed punctuations', 'result': analtext}
        #return render(request, 'analyse.html', params)
    if(capital =="on"):
        capitaltext=""
        for i in textdata:
            capitaltext= capitaltext + i.upper()
        textdata = capitaltext
        params = {'purpose':'Capitalised the text', 'result': capitaltext}
        #return render(request, 'analyse.html', params)
    if(charval == "on"):
        count = {}
        for i in textdata:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        params = {'purpose': 'Count of every character', 'result': count}
        #return render(request, 'analyse.html', params)
    return render(request, 'analyse.html', params)

