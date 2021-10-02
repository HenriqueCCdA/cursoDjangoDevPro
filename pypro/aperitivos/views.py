from django.shortcuts import render


def video(request, slug):
    print(slug)
    print(request)
    return render(request, 'aperitivos/video.html')
