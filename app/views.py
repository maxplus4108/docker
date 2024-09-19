from django.shortcuts import render, redirect
from urllib.parse import quote, unquote
def index_page(request):
    team = request.COOKIES.get('team', unquote('Не выбрано', encoding='utf-8'))
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')

    return render(request, 'index.html', {
        'theme': theme,
        'language': language,
        'team': team
    })
def save_settings(request):
    if request.method == 'POST':
        response = redirect('index')
        response.set_cookie('team', quote(request.POST.get('team'), encoding='utf-8'))
        response.set_cookie('theme', request.POST.get('theme'))
        response.set_cookie('language', request.POST.get('language'))
        return response
# Представление для страницы с таблицей сохраненных настроек
def settings_table(request):
    # Извлекаем сохраненные куки
    team = unquote(request.COOKIES.get('team', 'Не выбрано'), encoding='utf-8')
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    # Передаем данные в шаблон для отображения
    return render(request, 'settings_table.html', {
        'team': team,
        'theme': theme,
        'language': language
    })