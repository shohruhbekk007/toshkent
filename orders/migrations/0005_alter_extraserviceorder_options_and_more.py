# Generated by Django 4.0 on 2024-03-29 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_extraserviceorder_foodorder_stulorder_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraserviceorder',
            options={'ordering': ['id'], 'verbose_name': "Qo'shimcha xizmat", 'verbose_name_plural': "Qo'shimcha xizmatlar"},
        ),
        migrations.AlterModelOptions(
            name='foodorder',
            options={'ordering': ['id'], 'verbose_name': 'Ovqat buyurtma', 'verbose_name_plural': 'Ovqat buyurtmalar'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id'], 'verbose_name': 'Buyurtma', 'verbose_name_plural': 'Buyurtmalar'},
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['id'], 'verbose_name': 'Sotuv', 'verbose_name_plural': 'Sotuvlar'},
        ),
        migrations.AlterModelOptions(
            name='stulorder',
            options={'ordering': ['id'], 'verbose_name': 'Stul buyurtma', 'verbose_name_plural': 'Stul buyurtmalar'},
        ),
    ]
