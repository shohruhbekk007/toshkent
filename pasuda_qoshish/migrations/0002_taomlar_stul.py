# Generated by Django 4.0 on 2024-02-11 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pasuda_qoshish', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taomlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('Rasm', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('narxi', models.IntegerField()),
                ('toifasi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pasuda_qoshish.toifalash')),
            ],
        ),
        migrations.CreateModel(
            name='Stul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('olchami', models.CharField(blank=True, max_length=20, null=True)),
                ('Rasm', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('narxi', models.IntegerField()),
                ('toifasi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pasuda_qoshish.toifalash')),
            ],
        ),
    ]
