from django.shortcuts import render, get_object_or_404
from .models import Album, Songs
# Create your views here.
def index(request):
    html = ''
    all_album = Album.objects.all()
    # context = {
    # }
    return render(request, 'music/index.html', {"all_album": all_album})
def detail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {"album": album})
    # return HttpResponse("<h2>Details for Album id: " + str(album_id) + "<h2/>")
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except (KeyError, Songs.DoesNotExist):
        return render(request, 'music/detail.html',{
            "album":album,
            "error_message": "you did not selected favorite",
            })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {"album": album})
