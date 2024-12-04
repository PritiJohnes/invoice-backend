from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
# Create your views here.
from rest_framework import viewsets
from .models import Invoice,InvoiceDetail
from .serializers import InvoiceSerializer
from .serializers import InvoiceDetailSerializer
from django.http import HttpResponse
from rest_framework.views import APIView

def home(request):
    return HttpResponse("Welcome to the Home Page")

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer
    
class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    
class InvoiceListCreateView(APIView):
    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            if not request.data.get('date'):
              return Response({'error': 'Date field cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 