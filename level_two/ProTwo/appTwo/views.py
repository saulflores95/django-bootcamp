from django.shortcuts import render
from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'appTwo/users.html', context=user_dict)

def signup(request):
    form = NewUserForm()
    if(request.method == 'POST'):
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FROM INVALID')
    return render(request, 'appTwo/sign_up.html',{'form':form})
