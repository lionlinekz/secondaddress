from django.contrib import admin
from book.models import SubscriptionType, Subscription, PersonEmpowered, Day, Shopkeeper, UserProfile

admin.site.register(SubscriptionType)
admin.site.register(Subscription)
admin.site.register(PersonEmpowered)
admin.site.register(Day)
admin.site.register(Shopkeeper)
admin.site.register(UserProfile)
