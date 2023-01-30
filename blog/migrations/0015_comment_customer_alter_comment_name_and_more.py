# Generated by Django 4.1.5 on 2023-01-24 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_customer_address_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
