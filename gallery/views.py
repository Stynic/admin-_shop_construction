from django.shortcuts import render
from .models import Image, Video


def gallery(request):
    latest_question_list = Image.objects.order_by()[:]
    path_image = ['/'.join(elem.image.name.split('/')[1:]) for elem in latest_question_list]
    context = {'latest_question_list': path_image}
    return render(request, 'gallery/gallery.html', context)
