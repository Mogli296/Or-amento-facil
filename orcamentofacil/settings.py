"""
Django settings for orcamentofacil project.
Atualizado para Django 3.2 e compatível com Render.
"""

import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Segurança
# =========================
SECRET_KEY = os.environ.get("SECRET_KEY", "chave-insegura-dev")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

SITE_ID = 1

# =========================
# Aplicativos instalados
# =========================
INSTALLED_APPS = [
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps do projeto
    'orcamentos',
    'transportadoras',
    'cadastros',
    # pacotes externos
    'django_registration',   # corrigido
    'django_tables2',
    'crispy_forms',
    'django_countries',
    'localflavor',           # corrigido
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# =========================
# Middleware
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URLs e WSGI
# =========================
ROOT_URLCONF = 'orcamentofacil.urls'
WSGI_APPLICATION = 'orcamentofacil.wsgi.application'

# =========================
# Banco de dados
# =========================
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# =========================
# Internacionalização
# =========================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =========================
# Arquivos estáticos e mídia
# =========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# =========================
# Templates
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'static' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cadastros.context_processors.cadastros',
            ],
        },
    },
]

# =========================
# Email
# =========================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

# =========================
# Autenticação
# =========================
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 7
