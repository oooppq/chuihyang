from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'survey.html')

def first_survey(request):
    return render(request, 'first-index.html')

def form(request):
    return render(request, 'form.html')

def result(request):
    return render(request, 'result.html')