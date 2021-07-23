from django.http import Http404
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class QuoteListView(APIView):
    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class QuoteDetailView(APIView):
    def get_object(self, pk):
        try:
            return Quote.objects.get(pk = pk)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def put(self, request, pk):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data = serializer.data, status = status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data = serializer.data, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quote = self.get_object(pk)
        quote.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)