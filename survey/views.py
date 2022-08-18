from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'survey-index.html')

def survey1(request):
    return render(request, 'survey1.html')

def survey3(request):
    return render(request, 'survey3.html')

def form1(request):
    return render(request, 'form1.html')

def form3(request):
    return render(request, 'form3.html')

def result1(request):
    return render(request, 'result1.html')

def result3(request):
    return render(request, 'result3.html')

