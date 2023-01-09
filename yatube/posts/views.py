from django.http import HttpResponse

# Main page
def index(request):
    return HttpResponse('Главная страница')


# Страница groups_list
def group_posts(request, slug):
    return HttpResponse('Cтраниц сообщества {slug}')
