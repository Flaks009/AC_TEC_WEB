# Generated by Django 2.1.1 on 2018-10-31 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCad', '0007_auto_20181026_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nasc',
            field=models.DateField(verbose_name='Data de Nascimento (aaaa-mm-dd)'),
        ),
    ]