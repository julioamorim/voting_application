from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, request_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, request_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, request_id):
    return HttpResponse("You're voting on question %s." % question_id)