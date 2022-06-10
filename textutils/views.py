# I have created this file - Kishan

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params={'name':'KK', 'place':'Mars'}
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    
    print(djtext)
    #checking checkbox values
    removepunc = request.POST.get('removepunc','default')
    fullcaps = request.POST.get('fullcaps','default')
    newlinerem = request.POST.get('newlineremover','default')
    charcount = request.POST.get('charcount','default')
    
    # analyzed=djtext

    if removepunc == "on":
        punctuations='''!(){}[]-;:'"\,/<>.?@#$%^&*~`'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose': 'Removed Punctuatuion',
                'analyzed_text':analyzed}
        
        djtext=analyzed
       

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper();
        params={'purpose': 'Upper Case',
                'analyzed_text':analyzed}
        
        djtext=analyzed

    
    if(newlinerem=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        
        params={'purpose': 'New Line Remover',
                'analyzed_text':analyzed}
        
        djtext=analyzed
        
    
    if(charcount=="on"):
        analyzed=""
        c=0
        for char in djtext:
            if char != " ":
                c+=1

        params={'purpose': 'Char Count',
                'analyzed_text':c}
        

    if(removepunc != "on"  and  charcount!= "on"  and  newlinerem!= "on"):
        return render(request,'error.html')
    
    return render(request,'analyze.html',params)