from django.contrib import admin
from .models import Salesperson, Rating, Region


@admin.register(Salesperson)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'region')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('salesperson', 'rating', 'phone', 'sent_time')
    list_filter = ('salesperson',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
