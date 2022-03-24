from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    n = ['vlad', 'Belousov', 'Romanovich']
    return render(request, 'blog/index.html', context={'names': n})
    # return HttpResponse('<h1>Hello World</h1>')