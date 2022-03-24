from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>hello world</h1>')
    # print()
    # print(request)
    # print()
    # print(dir(request))
    # print()
    # pass
