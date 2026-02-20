"""Servicios de autenticación para el contexto CRM."""
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()


def authenticate_crm_user(username: str, password: str):
    """Autentica un usuario por username y password."""
    return authenticate(username=username, password=password)


def username_exists(username: str) -> bool:
    """Indica si ya existe un usuario con ese nombre."""
    return User.objects.filter(username=username).exists()


def create_crm_user(username: str, password: str):
    """Crea un usuario nuevo para el CRM."""
    return User.objects.create_user(username=username, password=password)
