from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

#Admin Header
admin.site.site_header = "NDF Administrator"

class ChapterA(admin.ModelAdmin):
    list_display = ('country', 'name', 'fee')

class Create_ChapterA(admin.ModelAdmin):
    list_display = ('user', 'name', 'country', 'state', 'city')

class Professional_GroupA(admin.ModelAdmin):
    list_display = ('name', 'objective', 'img', 'project')

class SliderA(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'img', 'desc')

class SuggestionA(admin.ModelAdmin):
    list_display = ('user', 'title')

class VoucherA(admin.ModelAdmin):
    list_display = ('voucher_code', 'voucher_type', 'amount', 'status')

class TeamA(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'img', 'designation')
    
class FAQa(admin.ModelAdmin):
    list_display = ('question', 'answer')
    
class ContactA(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    
class ProjectA(admin.ModelAdmin):
    list_display = ('title', 'img', 'desc')
    
class NewsA(admin.ModelAdmin):
    list_display = ('title', 'upload_date')
    
class donationsA(admin.ModelAdmin):
    list_display = ('user','frequency','donating_amount', 'email')

class endorsementA(admin.ModelAdmin):
    list_display = ('user','endorsed_by')
    
class membershipA(admin.ModelAdmin):
    list_display = ('user','email','chapter','professional_group','start_date', 'end_date')
    
class project_supportA(admin.ModelAdmin):
    list_display = ('user','package','paid_amount','start_date','end_date')

# Register your models here.
admin.site.register(Slider, SliderA)
admin.site.register(Chapter, ChapterA)
admin.site.register(Suggestion, SuggestionA)
admin.site.register(Create_Chapter, Create_ChapterA)
admin.site.register(Voucher, VoucherA)
admin.site.register(Professional_Group, Professional_GroupA)
admin.site.register(Team, TeamA)
admin.site.register(FAQ, FAQa)
admin.site.register(Contact, ContactA)
admin.site.register(Projects, ProjectA)
admin.site.register(New, NewsA)
admin.site.register(membership, membershipA)
admin.site.register(donations, donationsA)
admin.site.register(project_support, project_supportA)
admin.site.register(endorsement, endorsementA)
admin.site.register(UserProfile_new, SimpleHistoryAdmin)