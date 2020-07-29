from django.contrib import admin

from .models import DeclareWinners, Prediction

# Register your models here.

@admin.register(DeclareWinners)
class DeclareWinnersAdmin(admin.ModelAdmin):
    pass


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    pass

