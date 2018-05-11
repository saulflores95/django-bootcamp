from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My second project</em>")
def help(request):
    my_dict = {'help_page': "HELP PAGE"}
    return render(request, 'help/help.html', context=my_dict)
