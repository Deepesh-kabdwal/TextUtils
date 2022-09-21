# i have created this file -Deepesh
# from sqlite3 import paramstyle
# from string import punctuation



# import in django 
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Deepesh</h1> <a href="https://www.youtube.com/watch?v=C1Qi4ZWhInI">Hamsafar Link</a>''')

# def about(request):
#     return HttpResponse("a+b")



# functions created basically index and analyze
def index(request):
    # params={'name':'Deepesh','place':'mars'}
    return render(request,'index.html')



# function to analyze
def analyze(request):
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    # char_count=(request.POST.get('char_count','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    spaceremover=(request.POST.get('spaceremover','off'))
    # print(removepunc)
    # print(djtext)
    if(removepunc=="on"):
    # analyzed=djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%`~_^&*'''

        analyzed=" "
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

        # return render(request,'analyze.html',params)
    
    if(fullcaps=="on"):
        analyzed=" "
        for char in djtext:
            analyzed=analyzed+char.upper()
        
        params={'purpose':'change to uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    
    if(newlineremover=="on"):
        analyzed=" "
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        
        params={'purpose':'remove the newline from text','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    
    if(spaceremover == "on"):
        analyzed = " "
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)


    # if(char_count=="on"):
    #     count=0
    #     for char in djtext:
    #         count=count+1
        
    #     params={'purpose':'number of text in your string is','analyzed_text':count}
    #     djtext=analyzed
    #     # return render(request,'analyze.html',params)



    # if any one will not be followed then we will return the error
    if(removepunc !="on" and newlineremover !="on" and spaceremover !="on" and fullcaps !="on"): 
        return HttpResponse("please select any operation and try again")
    

    return render(request,'analyze.html',params)













# def capfirst(request):
#     return HttpResponse("capatalizefirst")

# def newlineremove(request):
#     return HttpResponse('newlineremover')

# def spaceremove(request):
#     return HttpResponse('''spaceremover <a href="/">back</a>''')

# def charcount(request):
#     return HttpResponse('charcount')
