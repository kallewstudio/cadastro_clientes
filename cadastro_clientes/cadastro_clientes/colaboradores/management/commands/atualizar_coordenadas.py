# colaboradores/management/commands/atualizar_coordenadas.py

from django.core.management.base import BaseCommand
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from cadastro_clientes.colaboradores.models import Colaborador
import time

class Command(BaseCommand):
    help = 'Atualiza as coordenadas de latitude e longitude para colaboradores já cadastrados'

    def handle(self, *args, **options):
        geolocator = Nominatim(user_agent="colaborador_geocoder")
        colaboradores_sem_coordenadas = Colaborador.objects.filter(latitude__isnull=True, longitude__isnull=True)

        for colaborador in colaboradores_sem_coordenadas:
            endereco_completo = f"{colaborador.endereco}, {colaborador.cidade}, {colaborador.cep}"
            try:
                location = geolocator.geocode(endereco_completo)
                if location:
                    colaborador.latitude = location.latitude
                    colaborador.longitude = location.longitude
                    colaborador.save()
                    self.stdout.write(self.style.SUCCESS(f"Coordenadas atualizadas para {colaborador.nome}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Não foi possível obter coordenadas para {colaborador.nome}"))
                time.sleep(1)  # Pausa para evitar limite de requisições
            except GeocoderTimedOut:
                self.stdout.write(self.style.ERROR(f"Tempo esgotado para {colaborador.nome}. Tente novamente."))
