# Generated by Django 3.2.9 on 2022-10-11 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Número')),
                ('plate', models.CharField(max_length=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('destiny', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destiny', to='location.location')),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origin', to='location.location')),
            ],
            options={
                'verbose_name': 'Autobús',
                'verbose_name_plural': 'Autobuses',
            },
        ),
    ]