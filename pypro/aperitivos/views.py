from django.shortcuts import render

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', youtube_id='4CNQuuQ0qWE'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', youtube_id='ScmQ4I5Qr5s')
]


videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
