from django.core.management.base import BaseCommand
from predictit2020_backend.models import Prediction

class Command(BaseCommand):
    help = 'Tallies up all the users predictions and compares them to the actual user'

    def handle(self, *args, **options):
        for prediction in Prediction.objects.all():
            prediction.calculate_number_of_states_right()
