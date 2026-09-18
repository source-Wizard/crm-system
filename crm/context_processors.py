from .models import Setting, Notification


def globals(request):
    try:
        setting = Setting.objects.first()
    except Exception:
        setting = None

    unread_notifications = 0
    try:
        if request.user.is_authenticated:
            unread_notifications = Notification.objects.filter(user=request.user, is_read=False).count()
    except Exception:
        unread_notifications = 0

    return {
        'app_setting': setting,
        'unread_notifications': unread_notifications,
        'currency_symbol': '$',
    }
