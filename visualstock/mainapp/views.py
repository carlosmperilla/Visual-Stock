from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'is_index' : True
    }
    # return HttpResponse("Un lindo inicio")
    return render(request, 'mainapp/index.html', context)