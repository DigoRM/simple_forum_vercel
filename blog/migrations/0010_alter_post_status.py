# Generated by Django 4.1.5 on 2023-01-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('active', 'active')], default='active', max_length=10),
        ),
    ]
