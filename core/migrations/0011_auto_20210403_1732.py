# Generated by Django 3.1.5 on 2021-04-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210403_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='horario_disponiveis',
            field=models.CharField(max_length=5),
        ),
    ]
