from django.shortcuts import get_object_or_404, redirect, render
from .models import Perfume

# Create your views here.

def post_check(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        perfumes = Perfume.objects.filter(name__contains=searched)
        if len(perfumes) >= 10:
            perfumes = perfumes[:10]
        
        return False
    return True
    
def home(request):
    flag = '0'
    if request.method == "GET":
        return render(request, 'index.html',{'is_searched':flag})
    elif request.method == "POST":
        searched = request.POST['searched']
        if searched != "": flag = '1'
        perfumes = Perfume.objects.filter(name__contains=searched)
        if len(perfumes) >= 10:
            perfumes = perfumes[:10]
        return render(request, 'index.html', {'perfumes':perfumes, 'searched':searched, 'is_searched':flag})
        

def perfumes(request, id):
    perfume = get_object_or_404(Perfume, id=id)
    return render(request, 'perfume.html', {"perfume":perfume})

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')

def survey(request):
    if request.method == "GET":
        return render(request, 'survey.html',{'is_searched':'0'})
    elif request.method == "POST":
        searched = request.POST['searched']
        perfumes = Perfume.objects.filter(name__contains=searched)
        if len(perfumes) >= 10:
            perfumes = perfumes[:10]
        return render(request, 'survey.html', {'perfumes':perfumes, 'searched':searched, 'is_searched':'1'})
    #flag = post_check(request)
    
    # if flag: return render(request, 'survey.html')

def reviews(request):
    return render(request, 'reviews.html')

def ranking(request):
    return render(request, 'ranking.html')