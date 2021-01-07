# I have created this file - Narender
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def navigation(request):
    ht = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>
            <a href="/"> Back </a>
            '''
    return HttpResponse(ht)

def about(request):
    return HttpResponse("This is about page")

def analyze(request):
    text = request.POST.get('text', 'default')
    rmf = request.POST.get('AnalyzeText', 'off')
    upp = request.POST.get('upper', 'off')
    spc = request.POST.get('spaceremove', 'off')
    nln = request.POST.get('newlineremove', 'off')
    # cou = request.POST.get('count', 'off')

    if rmf == "on":
        punc = '''!()-{}[];:'",<\>./?@#$%^&*~_'''
        pp = ""
        for char in text:
            if char not in punc:
                pp = pp + char
        params = {'abcd': 'Removed punctuations', 'xyz': pp}
        text = pp
        # return render(request, 'anlyze.html', params)

    if upp == "on":
        pp = ""
        for char in text:
            pp = pp + char.upper()
        params = {'abcd': 'Text Uppercase', 'xyz': pp}
        text = pp
        # return render(request, 'anlyze.html', params)

    if spc == "on":
        pp = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                pp = pp + char
        params = {'abcd': 'White space remove', 'xyz': pp}
        text = pp
        # return render(request, 'anlyze.html', params)

    if nln == "on":
        pp = ""
        for char in text:
            if char != "\n":
                pp = pp + char
        params = {'abcd': 'New Line remove', 'xyz': pp}
        # return render(request, 'anlyze.html', params)

    # elif cou == "on":
    #     pp = 'Char count is : ' + str(len(text))
    #     params = {'abcd': 'Char Count', 'xyz': pp}
    #     return render(request, 'anlyze.html', params)

    if rmf != "on" and upp != "on" and spc != "on" and nln != "on":
        return HttpResponse('<h2>Please selct the operation,Try again!<h2>')

    return render(request, 'anlyze.html', params)
