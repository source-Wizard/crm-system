"""
WSGI config for myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os
import shutil
from pathlib import Path
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

# Automatic database bootstrap for Vercel serverless environment
if os.environ.get('VERCEL'):
    try:
        base_dir = Path(__file__).resolve().parent.parent
        tmp_db = '/tmp/db.sqlite3'
        seed_db = base_dir / 'db_seed.sqlite3'
        if not os.environ.get('DATABASE_URL') and not os.environ.get('DB_HOST'):
            needs_copy = not os.path.exists(tmp_db)
            if not needs_copy and seed_db.exists():
                needs_copy = (seed_db.stat().st_size != os.path.getsize(tmp_db))
            if needs_copy and seed_db.exists():
                os.makedirs(os.path.dirname(tmp_db), exist_ok=True)
                shutil.copyfile(str(seed_db), tmp_db)
            elif not os.path.exists(tmp_db):
                from django.core.management import call_command
                call_command('migrate', interactive=False)
    except Exception as exc:
        print("Vercel DB bootstrap notice:", exc)

application = get_wsgi_application()
app = application

