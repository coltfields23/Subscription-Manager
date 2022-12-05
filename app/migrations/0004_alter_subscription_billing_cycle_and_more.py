# Generated by Django 4.1.2 on 2022-12-02 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_subscription_start_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='billing_cycle',
            field=models.CharField(blank=True, choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=20),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_day',
            field=models.CharField(blank=True, default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_month',
            field=models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('March', 'Mar'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Jan', max_length=10),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_year',
            field=models.CharField(blank=True, default='2022', max_length=10),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]