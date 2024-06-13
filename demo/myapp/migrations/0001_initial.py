# Generated by Django 5.0.4 on 2024-06-12 11:34

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benhnhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=100)),
                ('gioitinh', models.CharField(max_length=100)),
                ('namsinh', models.IntegerField()),
                ('diachi', models.CharField(max_length=100)),
                ('ngaykham', models.DateField(default='2024-01-01')),
            ],
        ),
        migrations.CreateModel(
            name='thietbiYte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('supplier', models.CharField(choices=[('Supplier A', 'Supplier A'), ('Supplier B', 'Supplier B'), ('Supplier C', 'Supplier C'), ('Supplier D', 'Supplier D'), ('Supplier E', 'Supplier E')], max_length=200)),
                ('import_date', models.DateField()),
                ('price', models.IntegerField()),
                ('purpose', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Thuoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenThuoc', models.CharField(max_length=50)),
                ('giatheovien', models.IntegerField()),
                ('giatheochai', models.IntegerField()),
                ('soviencon', models.IntegerField()),
                ('sochaicon', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('receptionist', 'Lễ tân'), ('doctor', 'Bác sĩ'), ('hr_manager', 'Quản lý nhân sự'), ('warehouse_manager', 'Quản lý kho')], max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hoadon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tienkham', models.IntegerField()),
                ('tienthuoc', models.IntegerField()),
                ('benhnhan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.benhnhan')),
            ],
        ),
        migrations.CreateModel(
            name='PhieuKB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trieuchung', models.CharField(max_length=100)),
                ('dudoan', models.CharField(max_length=100)),
                ('benhnhan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.benhnhan')),
            ],
        ),
        migrations.CreateModel(
            name='PKBthuoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donvi', models.CharField(max_length=50)),
                ('soluong', models.IntegerField()),
                ('cachdung', models.CharField(max_length=50)),
                ('phieukb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.phieukb')),
                ('thuoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.thuoc')),
            ],
        ),
    ]
