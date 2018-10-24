# Generated by Django 2.1.1 on 2018-10-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('curso', models.CharField(max_length=100, verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'nome',
                'verbose_name_plural': 'nomes',
                'ordering': ['nome'],
            },
        ),
    ]
