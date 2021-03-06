# Generated by Django 3.2.9 on 2021-11-28 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30, verbose_name='Modelo do Veículo:')),
                ('marca', models.CharField(max_length=30, verbose_name='Meca do Veículo:')),
                ('ano', models.IntegerField(verbose_name='Ano do Veículo:')),
                ('tipo', models.IntegerField(choices=[(1, 'Manutenção da Embreagem'), (2, 'Revisão dos componentes de freio'), (3, 'Revisão do Sistema de Arrefecimento'), (4, 'Troca de óleo do motor'), (5, 'Troca de óleo do câmbio automático'), (6, 'Troca de filtros'), (7, 'Troca de lâmpadas'), (8, 'Alinhamento e Balanceamento')], verbose_name='Tipo de Serviços:')),
                ('tempo_conserto', models.IntegerField(verbose_name='Tempo de Conserto:')),
                ('valor', models.CharField(max_length=9, verbose_name='Valor do Serviço: R$')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('ano', models.IntegerField()),
                ('placa', models.CharField(max_length=8)),
                ('data_insp', models.DateField(verbose_name='Data da Inspeção')),
                ('horario', models.IntegerField(choices=[(8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'), (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00')], verbose_name='Horario da Inspeção')),
                ('descricao', models.TextField(verbose_name='Descrição do Problema')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
    ]
