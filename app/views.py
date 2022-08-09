from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Perfume, Review
from .forms import ReviewForm

from django.db.models import Q
# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'index.html', {'is_searched': '0'})
    elif request.method == "POST":
        season_list = request.POST.getlist('season_list')  # ['summer']
        flavor_list = request.POST.getlist('flavor_list') # ['woody']
        gender_list = request.POST.getlist('gender_list') # ['man']

        searched = request.POST['searched']

        if searched:
            perfumes = Perfume.objects.filter(name__contains=searched)
            if len(perfumes) >= 10:
                perfumes = perfumes[:10]
            return render(request, 'index.html', {'perfumes': perfumes, 'searched': searched, 'is_searched': '1'})

        else:
            query = Q()
            for Season in season_list:
                query = query | Q(season=Season)
            for Flavor in flavor_list:
                query = query | Q(flavor=Flavor)
            for Gender in gender_list:
                query = query | Q(gender=Gender)
            perfumes = Perfume.objects.filter(query)
            return render(request, 'search_result.html', {'perfumes': perfumes})
        # return redirect('perfumes', perfume[0].pk)

def filter_search(request):
    season_list = request.GET.getlist('season_list')  # ['summer']
    flavor_list = request.GET.getlist('flavor_list') # ['woody']
    gender_list = request.GET.getlist('gender_list') # ['man']
    searched = request.GET['searched']
    perfumes = Perfume.objects.filter(name__contains=searched)

    query = Q()
    for Season in season_list:
        query = query | Q(season=Season)
    for Flavor in flavor_list:
        query = query | Q(flavor=Flavor)
    for Gender in gender_list:
        query = query | Q(gender=Gender)
    perfumes = perfumes.objects.filter(query)
    return render(request, 'searched-list.html', {'perfumes': perfumes})

def perfumes(request, id):
    perfume = get_object_or_404(Perfume, id=id)
    review_form = ReviewForm()
    return render(request, 'perfume.html', {"perfume": perfume, "review_form": review_form})


def new_review(request, id):
    filled_form = ReviewForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.perfume = get_object_or_404(Perfume, id=id)
        finished_form.save()
    return redirect('perfumes', id)


def about(request):
    return render(request, 'about.html')


def category(request):
    return render(request, 'category.html')


def survey(request):
    return render(request, 'survey.html')


def reviews(request):
    return render(request, 'reviews.html')


def ranking(request):
    return render(request, 'ranking.html')

#### show real time search result ####
def search(request):
    searched = request.GET['searched']
    perfumes = Perfume.objects.filter(name__contains=searched)
    perfumeList = [(p.id, p.name) for p in perfumes[:10]]
    data = {'searchedList': perfumeList}
    return JsonResponse(data)

#### search result page ####
def searched(request):
    searched = request.GET['searched']
    print(searched)
    perfumes = Perfume.objects.filter(name__contains=searched)
    return render(request, 'searched-list.html', {'searched':searched,'perfumes':perfumes})