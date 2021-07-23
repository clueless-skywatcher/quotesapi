from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all().order_by('name')
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]