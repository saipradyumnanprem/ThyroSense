from django.contrib import admin
from Home.models import UserProfile, UserReport, Doctor


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'address', 'phone_number', 'last_upd')


class UserReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 't3', 'tt4', 't4u', 'fti', 'sex', 'sick',
                    'pregnant', 'thyroid_surgery', 'goitre', 'tumor', 'category')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'bio')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserReport, UserReportAdmin)
admin.site.register(Doctor, DoctorAdmin)
