# Generated by Django 4.1.4 on 2023-02-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_category_status_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('draft', 'draft')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('draft', 'draft')], default='active', max_length=10),
        ),
    ]