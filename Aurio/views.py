from django.shortcuts import render
from Aurio.models import TSong,Song,OldSong,Watchlater,Channel,USong
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.db.models import Case, When   

def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs =song.filter(name__icontains=query)
    return render(request, 'Aurio/search.html', {"songs":qs})

def index(request):
    usong = USong.objects.all()
    tsong = TSong.objects.all()
    song = Song.objects.all()
    oldsong = OldSong.objects.all()
    return render(request, 'index.html',{'oldsong':oldsong ,'usong':usong ,'tsong':tsong ,'song':song})

def songs(request):
    usong = USong.objects.all()
    tsong = TSong.objects.all()
    song = Song.objects.all()
    oldsong = OldSong.objects.all()
    return render(request,'Aurio/songs.html',{'oldsong':oldsong ,'usong':usong ,'tsong':tsong ,'song':song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'Aurio/songpost.html',{'song':song})

def tsongpost(request, id):
    tsong = TSong.objects.filter(song_id=id).first()
    return render(request,'Aurio/tsongpost.html',{'song':tsong})

def usongpost(request, id):
    usong = USong.objects.filter(song_id=id).first()
    return render(request,'Aurio/usongpost.html',{'usong':usong})

def oldsongpost(request, id):
    oldsong = OldSong.objects.filter(song_id=id).first()
    return render(request,'Aurio/oldsongpost.html',{'song':oldsong})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request,user)
        redirect("/")
    return render(request, 'Aurio/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password= pass2)
        from django.contrib.auth import login
        login(request,user)
        
        channel = Channel(name=username)
        channel.save()

        
        return redirect('/')
    return render(request,'Aurio/signup.html')

def channel(request, channel):
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(video_ids)])
    usong = USong.objects.filter(song_id__in=video_ids).order_by(preserved)    

    return render(request, "Aurio/channel.htm", {"channel": chan, "usong": usong})

def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        singer = request.POST['singer']
        tag = request.POST['tag']
        image = request.POST['image']
        movie = request.POST['movie']
        song1 = request.FILES['file']

        song_model = Song(name=name, singer=singer, tags=tag, image=image, movie=movie, song=song1)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))
        print(channel_find)

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()

    return render(request, "Aurio/upload.html")


def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Watchlater.objects.filter(user=user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "Your Song is Already Added"
                break
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            message = "Your Song is Succesfully Added"

        song = Song.objects.filter(song_id=video_id).first()
        tsong = TSong.objects.filter(song_id=video_id).first()
        return render(request,f"Aurio/songpost.html", {'song':song,'tsong':tsong,"message": message})

    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)
    tsong = TSong.objects.filter(song_id__in=ids).order_by(preserved)
    return render(request, "Aurio/watchlater.html", {'song': song,'tsong':tsong})



            