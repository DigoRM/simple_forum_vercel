# Generated by Django 4.1.4 on 2023-02-04 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_category_intro_alter_category_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('active', 'active')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('active', 'active')], default='active', max_length=10),
        ),
    ]
