# context_processors.py

from .models import Notification

def unread_notifications(request):
    if request.user.is_authenticated:
        has_unread = Notification.objects.filter(user=request.user, is_read=False).exists()
        print(f"Has unread notifications: {has_unread}")  # Remove or change to logging in production
        return {'has_unread_notifications': has_unread}
    return {'has_unread_notifications': False}


