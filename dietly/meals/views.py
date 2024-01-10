from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Meals
from django.shortcuts import get_object_or_404, render

from .macro import calculateMacro
from .days import currentWeekRange, currentWeek, specificWeekRange


def index(request):
    # #latest_meals_list = Meals.objects.order_by("date")[:5555]
    # start,end = currentWeekRange()
    # #start,end = specificWeekRange(2)
    # #latest_meals_list = Meals.objects.filter(date__range=["2024-01-01","2024-01-10"]).order_by("date")
    # latest_meals_list = Meals.objects.filter(date__range=[start,end]).order_by("date")

    # context             = calculateMacro(latest_meals_list)
    # context["week"]     = currentWeek()
    # context["nextWeek"] = currentWeek()+1

    return week(request, currentWeek())
    return render(request, "meals/index.html", context)

def detail(request, id):
    try:
        meal = Meals.objects.get(id=id)
        ingredients=meal.ingredients.split("'")[1::2]

    except Meals.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "meals/detail.html", {"meal": meal, "ingredients": ingredients})

def week(request, id):
    start,end = specificWeekRange(id)
    latest_meals_list = Meals.objects.filter(date__range=[start,end]).order_by("date")

    context                 = calculateMacro(latest_meals_list)
    context["week"]         = id
    context["nextWeek"]     = id+1
    context["previousWeek"] = id-1

    return render(request, "meals/index.html", context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)