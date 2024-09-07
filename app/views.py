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
# Представление для страницы с таблицей сохраненных настроек
def settings_table(request):
    # Извлекаем сохраненные куки
    team = request.COOKIES.get('team', 'Не выбрано')
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')

    # Передаем данные в шаблон для отображения
    return render(request, 'settings_table.html', {
        'team': team,
        'theme': theme,
        'language': language
    })