# Generated by Django 2.2 on 2020-02-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tarefas', '0002_delete_tarefa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
