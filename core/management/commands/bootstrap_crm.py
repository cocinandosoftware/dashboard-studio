from django.core.management.base import BaseCommand

from core.perfiles.models import Perfil
from core.tipos_accion.models import TipoAccion


class Command(BaseCommand):
    help = 'Carga catálogos iniciales del CRM (perfiles y tipos de acción).'

    def handle(self, *args, **options):
        perfiles_iniciales = [
            {'nombre': 'Administrador', 'tipo': Perfil.Tipo.ADMIN},
            {'nombre': 'Gerente', 'tipo': Perfil.Tipo.GERENTE},
            {'nombre': 'Comercial', 'tipo': Perfil.Tipo.COMERCIAL},
        ]

        tipos_accion_iniciales = [
            'Llamada',
            'Visita',
            'Email',
            'WhatsApp',
            'Reunión',
        ]

        perfiles_creados = 0
        for perfil_data in perfiles_iniciales:
            _, created = Perfil.objects.get_or_create(
                tipo=perfil_data['tipo'],
                defaults={
                    'nombre': perfil_data['nombre'],
                    'activo': True,
                },
            )
            if created:
                perfiles_creados += 1

        tipos_creados = 0
        for nombre_tipo in tipos_accion_iniciales:
            _, created = TipoAccion.objects.get_or_create(
                nombre=nombre_tipo,
                defaults={'activo': True},
            )
            if created:
                tipos_creados += 1

        self.stdout.write(self.style.SUCCESS('Bootstrap CRM completado.'))
        self.stdout.write(
            self.style.SUCCESS(
                f'Perfiles creados: {perfiles_creados} | Tipos de acción creados: {tipos_creados}'
            )
        )
