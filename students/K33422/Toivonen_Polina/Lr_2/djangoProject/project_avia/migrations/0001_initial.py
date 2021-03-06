# Generated by Django 3.1.5 on 2021-01-21 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('contacts', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('type', models.CharField(choices=[('up', 'отправление'), ('down', 'прибытие')], max_length=15)),
                ('gate_num', models.CharField(max_length=5)),
                ('flight_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_avia.company')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('kind', models.CharField(choices=[('gate', 'Изменение gate №'), ('depart', 'Проблемы с прилетом'), ('arrive', 'Проблемы с отправлением'), ('lost', 'Потерявшийся пассажир')], max_length=25)),
                ('flight_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_avia.flight')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
