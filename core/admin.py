from django.contrib import admin
from core.models import RegistrationForm, MainContent, DocterDetails, Awarded_By, Framework_Steps, How_Will_This, Get_Bonuses, Who_Attend, About_Your_Health_Coach, Your_Health_Coach_Awarded, FAQs, How_Does_This


# Main Content Section Admin.
@admin.register(MainContent)
class MainContent(admin.ModelAdmin):
    list_display = ['id', 'Main_Title', 'Second_Content', 'Third_Content']


# Docter Details Section Admin.
admin.site.register(DocterDetails)


# Awarded By Section.
admin.site.register(Awarded_By)

# Framework_Steps  Section Admin
admin.site.register(Framework_Steps)

# How_Will_This Admin.
admin.site.register(How_Will_This)


# Get_Bonuses Admin.
admin.site.register(Get_Bonuses)


# Who_Attend Admin.
admin.site.register(Who_Attend)

# About_Your_Health_Coach Admin.
admin.site.register(About_Your_Health_Coach)



# Your_Health_Coach_Awarded Admin.
admin.site.register(Your_Health_Coach_Awarded)


# FAQs Admin.
admin.site.register(FAQs)



# How_Does_This Admin.
admin.site.register(How_Does_This)


# RegistrationForm Section Admin.
@admin.register(RegistrationForm)
class RegistrationForm(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'location']