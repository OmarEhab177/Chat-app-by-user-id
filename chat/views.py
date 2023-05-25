from django.shortcuts import render

from django.shortcuts import render
from .models import User


def select_user(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/select_user.html', {'users': users, 'current_user_id': request.user.id})

def chat_page(request):
    current_user_id = request.GET.get('current_user_id')
    other_user_id = request.GET.get('other_user_id')
    return render(request, 'chat/chat_page.html', {'user_id': current_user_id, 'other_user_id': other_user_id})
