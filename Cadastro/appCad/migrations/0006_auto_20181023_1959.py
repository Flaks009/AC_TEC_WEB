# Generated by Django 2.1.1 on 2018-10-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCad', '0005_auto_20181023_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nasc',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
    ]