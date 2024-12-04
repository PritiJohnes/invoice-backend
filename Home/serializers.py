from rest_framework.views import APIView
from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description', 'quantity', 'unit_price', 'line_total']
        read_only_fields = ['line_total']  # Line total is computed

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice
    
class InvoiceListCreateView(APIView):
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

























# from rest_framework import serializers
# from .models import Invoice, InvoiceDetail

# # Serializer for InvoiceDetail
# class InvoiceDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InvoiceDetail
#         fields =  ['id', 'invoice', 'description', 'quantity', 'unit_price', 'line_total']
    
     
     
     
     
# # class InvoiceSerializer(serializers.ModelSerializer):
# #      details = InvoiceDetailSerializer(many=True)  # Remove `read_only=True`
 
# #      class Meta:
# #         model = Invoice
# #         fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']
 
# #      def create(self, validated_data):
# #         details_data = validated_data.pop('details')
# #         invoice = Invoice.objects.create(**validated_data)
 
# #         for detail_data in details_data:
# #             InvoiceDetail.objects.create(invoice=invoice, **detail_data)
 
# #         return invoice
     
     
     
# class InvoiceSerializer(serializers.ModelSerializer):
#     details = InvoiceDetailSerializer(many=True)

#     class Meta:
#         model = Invoice
#         fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']
        
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         # Format the date if necessary
#         if representation['date']:
#             representation['date'] = representation['date'][:10]  # This will format it as 'YYYY-MM-DD'
#         return representation
    
#     def create(self, validated_data):
#         details_data = validated_data.pop('details', [])
#         invoice = Invoice.objects.create(**validated_data)
#         for detail_data in details_data:
#             InvoiceDetail.objects.create(invoice=invoice, **detail_data)
#         return invoice

#     def update(self, instance, validated_data):
#         details_data = validated_data.pop('details', [])
#         instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
#         instance.customer_name = validated_data.get('customer_name', instance.customer_name)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()

#         # Update or create invoice details
#         for detail_data in details_data:
#             detail_id = detail_data.get('id')
#             if detail_id:
#                 # Update existing detail
#                 detail = InvoiceDetail.objects.get(id=detail_id, invoice=instance)
#                 for key, value in detail_data.items():
#                     setattr(detail, key, value)
#                 detail.save()
#             else:
#                 # Create new detail
#                 InvoiceDetail.objects.create(invoice=instance, **detail_data)

#         return instance