"""
"""
import os
import sys

if __name__ == "__main__":
    CURRENT = os.path.dirname(__file__)
    CURRENT = os.path.realpath(os.path.join(CURRENT, '..'))
    CURRENT = os.path.realpath(os.path.join(CURRENT, '..'))

    sys.path.insert(0, CURRENT)
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'redirect_test.settings_local')

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        User.objects.get(username='root')
    except User.DoesNotExist:
        User.objects.create_superuser('root', 'admin@myproject.com', 'root')
        print('**************************************************')
        print('**************************************************')
        print('Superuser created. root/root')
        print('**************************************************')
        print('**************************************************')
