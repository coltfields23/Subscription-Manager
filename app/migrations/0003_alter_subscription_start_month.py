# Generated by Django 4.1.2 on 2022-12-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_subscription_monthly_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='start_month',
            field=models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('March', 'Mar'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('Aug', 'Aug'), ('Sept', 'Sept'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Jan', max_length=10),
        ),
    ]
