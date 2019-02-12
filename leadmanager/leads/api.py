from .models import Lead
from rest_framework import viewsets,permissions

from leads.serializers import LeadSerializer

#LEADVSET
class LeadViewSet(viewsets.ModelViewSet):        
    queryset=Lead.objects.all()
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class=LeadSerializer
    def get_queryset(self):
        return self.request.user.leads.all()

    def perfom_create(self,serializer):
        serializer.save(owner=self.request.user)
    
