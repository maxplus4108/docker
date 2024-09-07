from django.shortcuts import render, redirect

def index_page(request):
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    last_team = request.COOKIES.get('team', '')

    return render(request, 'index.html', {
        'theme': theme,
        'language': language,
        'team': last_team
    })
def save_settings(request):
    if request.method == 'POST':
        response = redirect('index')
        response.set_cookie('team', request.POST.get('team'))
        response.set_cookie('theme', request.POST.get('theme'))
        response.set_cookie('language', request.POST.get('language'))
        return response
    