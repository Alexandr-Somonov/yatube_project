from django.shortcuts import render
from django.template import loader

# Main page
def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': "Это главная страница проекта Yatube",
    }
    return render(request, template, context)


# Страница groups_list
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Лев Толстой – зеркало русской революции."
    context = {
        'title': title,
        'text': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)
