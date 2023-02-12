from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Shareyar', 'place': 'Bangladesh'}
    return render(request, 'index.html', params)

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    rempunc = request.POST.get('rempuncbtn', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if rempunc == 'on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removing punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyzed.html', params)

    if (capitalize == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Covert to upper', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyzed.html', params)

    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                print('No')
        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyzed.html', params)

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1]) == ' ':
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyzed.html', params)

    if (charcount == 'on'):
        analyzed = analyzed + '\nTotal Characters:' + str(len(djtext))

        params = {'purpose': 'Characters counted', 'analyzed_text': analyzed}


    if (rempunc != 'on' and capitalize != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse("Error! Please select minimum one operation.")

    return render(request, 'analyzed.html', params)