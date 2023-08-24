from django.contrib import admin
from .models import Review
from .models import Cafe, Rest, Place, Addr
from .forms import ReviewWrite
# Register your models here.
admin.site.register(Cafe)
admin.site.register(Rest)
admin.site.register(Place)
admin.site.register(Addr)

@admin.register(Review)
class ReviewAmin(admin.ModelAdmin):
    form = ReviewWrite