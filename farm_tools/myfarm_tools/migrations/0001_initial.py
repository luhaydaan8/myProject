# myfarm_tools/migrations/0001_initial.py
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        # If there are any dependencies (e.g., 'auth', '0002_auto_20230901_1123'), list them here.
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tool_type', models.CharField(choices=[('manual', 'Manual'), ('mechanical', 'Mechanical')], max_length=50)),
                ('condition', models.CharField(choices=[('new', 'New'), ('used', 'Used'), ('damaged', 'Damaged')], max_length=50)),
                ('purchase_date', models.DateField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('under_repair', 'Under Repair')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('role', models.CharField(choices=[('owner', 'Owner'), ('worker', 'Worker')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField(default=django.utils.timezone.now)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('returned', 'Returned'), ('overdue', 'Overdue')], max_length=50)),
                ('farmer', models.ForeignKey(on_delete=models.CASCADE, to='myfarm_tools.farmer')),
                ('tool', models.ForeignKey(on_delete=models.CASCADE, to='myfarm_tools.tool')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField()),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tool', models.ForeignKey(on_delete=models.CASCADE, to='myfarm_tools.tool')),
                ('performed_by', models.ForeignKey(on_delete=models.CASCADE, to='myfarm_tools.farmer')),
            ],
        ),
    ]
