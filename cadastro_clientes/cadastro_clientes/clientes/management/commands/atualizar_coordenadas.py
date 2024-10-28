# cadastro_clientes/clientes/management/commands/atualizar_coordenadas.py

from django.core.management.base import BaseCommand
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from cadastro_clientes.clientes.models import Empresa
import time

class Command(BaseCommand):
    help = 'Atualiza as coordenadas de latitude e longitude para empresas já cadastradas'

    def handle(self, *args, **options):
        geolocator = Nominatim(user_agent="empresa_geocoder")
        empresas_sem_coordenadas = Empresa.objects.filter(latitude__isnull=True, longitude__isnull=True)

        for empresa in empresas_sem_coordenadas:
            endereco_completo = f"{empresa.endereco}, {empresa.cidade}, {empresa.cep}"
            try:
                location = geolocator.geocode(endereco_completo)
                if location:
                    empresa.latitude = location.latitude
                    empresa.longitude = location.longitude
                    empresa.save()
                    self.stdout.write(self.style.SUCCESS(f"Coordenadas atualizadas para {empresa.nome}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Não foi possível obter coordenadas para {empresa.nome}"))
                time.sleep(1)  # Pausa para evitar limite de requisições
            except GeocoderTimedOut:
                self.stdout.write(self.style.ERROR(f"Tempo esgotado para {empresa.nome}. Tente novamente."))
