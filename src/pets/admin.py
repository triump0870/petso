from django.contrib import admin
from pets.models import Pet


# Register your models here.

class PetAdmin(admin.ModelAdmin):
    def queryset(self, request):
        """Limit pets to those that belong to the request's user."""
        qs = super(PetAdmin, self).queryset(request)
        print(qs)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


admin.site.register(Pet, PetAdmin)
