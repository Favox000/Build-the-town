from django.shortcuts import render
from .models import Message
from django.contrib.auth.models import User
from account.models import Profile
from django.utils import timezone

# Create your views here.
def chat(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        content = request.POST.get('content')
        now = timezone.now()
        if content:
            message = Message(content=content, sendet_by=user.username, created_at=now)
            message.save()

    return render(request, 'chat/chat.html', {
        'messages': Message.objects.all()[::-1],
        'profile' : profile,
        'username': user.username,
    })