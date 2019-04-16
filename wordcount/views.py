from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
def homepage(request):
    return render(request, 'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    count = fulltext.split()
    alllist = {}
    for word in count:
        if word in alllist:
            alllist[word] = alllist[word] + 1
        else:
            alllist[word] = 1
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(count),'alllist':alllist.items()})
