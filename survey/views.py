from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'survey-index.html')

def survey1(request):
    return render(request, 'survey1.html')

def form1(request):
    return render(request, 'form1.html')

def result1(request):
    return render(request, 'result1.html')