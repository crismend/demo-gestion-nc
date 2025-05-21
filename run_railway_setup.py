# run_railway_setup.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from django.core.management import call_command

print("📦 Ejecutando migraciones...")
call_command("migrate")

print("👤 Verificando superusuario...")
from django.contrib.auth import get_user_model
User = get_user_model()

username = "admin"
email = "admin@demo.com"
password = "admin123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superusuario creado: admin / admin123")
else:
    print("ℹ️ Superusuario ya existe.")
