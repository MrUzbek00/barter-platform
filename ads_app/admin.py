from django.contrib import admin
from .models import Ad, ExchangeProposal

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'condition', 'user', 'created_at')
    search_fields = ('title', 'category', 'description', 'user__username')
    list_filter = ('condition', 'category')

class ExchangeProposalAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad_sender', 'ad_receiver', 'status', 'created_at')
    search_fields = ('ad_sender__title', 'ad_receiver__title', 'comment')
    list_filter = ('status',)

admin.site.register(Ad, AdAdmin)
admin.site.register(ExchangeProposal, ExchangeProposalAdmin)
