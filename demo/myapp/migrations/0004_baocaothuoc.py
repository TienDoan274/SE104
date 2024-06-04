# Generated by Django 5.0.3 on 2024-06-04 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_thietbiyte_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaoCaoThuoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thuoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.thuoc')),
            ],
        ),
    ]
