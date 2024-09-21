from django.shortcuts import render
from Aurio.models import TSong, Song, OldSong,USong
def index(request):
    oldsong= OldSong.objects.all()
    tsong= TSong.objects.all()
    usong= USong.objects.all()
    song = Song.objects.all()
    return render(request, 'index.html', {'oldsong':oldsong ,'usong':usong ,'tsong':tsong , 'song': song})



    


