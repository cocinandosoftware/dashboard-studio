"""Validadores de autenticación sin formularios de Django."""
import re


USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9_]+$")


def validate_access_data(username: str, password: str) -> dict:
    """Valida datos mínimos para acceso."""
    errors = {
        'username': [],
        'password': [],
        'non_field': [],
    }

    if not username:
        errors['username'].append('El usuario es obligatorio.')

    if not password:
        errors['password'].append('La contraseña es obligatoria.')

    return errors


def validate_register_data(username: str, password1: str, password2: str) -> dict:
    """Valida datos mínimos para registro."""
    errors = {
        'username': [],
        'password1': [],
        'password2': [],
        'non_field': [],
    }

    if not username:
        errors['username'].append('El usuario es obligatorio.')
    elif len(username) < 3:
        errors['username'].append('El usuario debe tener al menos 3 caracteres.')
    elif not USERNAME_REGEX.match(username):
        errors['username'].append('El usuario solo puede contener letras, números y guion bajo.')

    if not password1:
        errors['password1'].append('La contraseña es obligatoria.')
    elif len(password1) < 8:
        errors['password1'].append('La contraseña debe tener al menos 8 caracteres.')

    if not password2:
        errors['password2'].append('Debes confirmar la contraseña.')

    if password1 and password2 and password1 != password2:
        errors['password2'].append('Las contraseñas no coinciden.')

    return errors


def has_validation_errors(errors: dict) -> bool:
    """Indica si hay errores en cualquier campo."""
    return any(bool(messages) for messages in errors.values())
