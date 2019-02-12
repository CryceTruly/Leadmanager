
from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "Leads Adminstration"
admin.site.site_title = "Lead Manager Portal"
admin.site.index_title = "Welcome to LeadManager"

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',include('leads.urls')),
    path('',include('accounts.urls'))
    
]
