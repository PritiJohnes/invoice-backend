from django.db import models

# Create your models here.
# model1
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number=models.CharField(max_length=100,unique=True)
    customer_name=models.CharField(max_length=255)
    date=models.DateField(null=True, blank=True)
    def __str__(self):
        return self.invoice_number
# Model 2: InvoiceDetail
class InvoiceDetail(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)