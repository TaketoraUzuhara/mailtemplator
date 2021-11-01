from django.shortcuts import render
from .forms import MailForm

def home(request):
    params = {'template': '', 'title': '', 'content': '', 'form': None}
    if request.method == "POST":
        form = MailForm(request.POST)
        params['template'] = request.POST["template"]
        params['title'] = request.POST["title"]
        params['content'] = request.POST["content"]
        params['form'] = form
    else:
        params['form'] = MailForm()
    return render(request, "home.html", params)