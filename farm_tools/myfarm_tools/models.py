from django.db import models
from django.utils import timezone

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    tool_type = models.CharField(max_length=50, choices=[('manual', 'Manual'), ('mechanical', 'Mechanical')])
    condition = models.CharField(max_length=50, choices=[('new', 'New'), ('used', 'Used'), ('damaged', 'Damaged')])
    purchase_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('under_repair', 'Under Repair')])

    def __str__(self):
        return self.name


class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=256)
    phone_number = models.IntegerField(max_length=15)
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Loan(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('returned', 'Returned'), ('overdue', 'Overdue')])

    def __str__(self):
        return f'{self.farmer} borrowed {self.tool} on {self.loan_date}'

    def is_overdue(self):
        if self.return_date is None and self.loan_date < timezone.now().date():
            return True
        return False


class Maintenance(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    performed_by = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return f'Maintenance for {self.tool} on {self.maintenance_date}'



