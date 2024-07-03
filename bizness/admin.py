from django.contrib import admin

# Register your models here.
from .models import Card, CardDescription, Subscription

class CardDescriptionInline(admin.TabularInline):
    model = CardDescription
    extra = 1  # Number of extra forms to display

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    inlines = [CardDescriptionInline]
    list_display = ("title", 'price', 'get_description')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "card")
