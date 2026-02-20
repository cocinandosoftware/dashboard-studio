"""Vistas de acceso para el contexto CRM."""
from django.contrib.auth import login
from django.shortcuts import redirect, render
from library.services.auth_service import (
    authenticate_crm_user,
    create_crm_user,
    username_exists,
)
from library.validators.auth_validators import (
    has_validation_errors,
    validate_access_data,
    validate_register_data,
)


def access_view(request):
    """Vista CRM para autenticación de usuarios."""
    if request.user.is_authenticated:
        return redirect('public:hello_world')

    form_data = {
        'username': '',
    }
    errors = {
        'username': [],
        'password': [],
        'non_field': [],
    }

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        form_data['username'] = username

        errors = validate_access_data(username=username, password=password)
        if not has_validation_errors(errors):
            user = authenticate_crm_user(username=username, password=password)
            if user is None:
                errors['non_field'].append('Usuario o contraseña incorrectos.')
            else:
                login(request, user)
                return redirect('public:hello_world')

    return render(
        request,
        'access.html',
        {
            'titulo': 'Acceso CRM',
            'form_data': form_data,
            'errors': errors,
        }
    )


def register_view(request):
    """Vista CRM para registro y validación de nuevo usuario."""
    if request.user.is_authenticated:
        return redirect('public:hello_world')

    form_data = {
        'username': '',
    }
    errors = {
        'username': [],
        'password1': [],
        'password2': [],
        'non_field': [],
    }

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        form_data['username'] = username

        errors = validate_register_data(
            username=username,
            password1=password1,
            password2=password2,
        )

        if not has_validation_errors(errors):
            if username_exists(username):
                errors['username'].append('El usuario ya existe.')
            else:
                user = create_crm_user(username=username, password=password1)
                login(request, user)
                return redirect('public:hello_world')

    return render(
        request,
        'register.html',
        {
            'titulo': 'Registro CRM',
            'form_data': form_data,
            'errors': errors,
        }
    )
