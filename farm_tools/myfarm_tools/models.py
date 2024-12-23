from django.db import models
from django.utils import timezone

# Tool Model - represents farm tools that can be borrowed
class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tool_type = models.CharField(max_length=50, choices=[('manual', 'Manual'), ('mechanical', 'Mechanical')])
    condition = models.CharField(max_length=50, choices=[('new', 'New'), ('used', 'Used'), ('damaged', 'Damaged')])
    purchase_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('under_repair', 'Under Repair')])

    def __str__(self):
        return self.name

# Farmer Model - represents farmers who borrow the tools
class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=50, choices=[('owner', 'Owner'), ('worker', 'Worker')])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Loan Model - tracks the borrowing of tools by farmers
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

# Maintenance Model - tracks maintenance performed on tools
class Maintenance(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    performed_by = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return f'Maintenance for {self.tool} on {self.maintenance_date}'
