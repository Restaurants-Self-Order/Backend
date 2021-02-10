# Generated by Django 3.1.4 on 2021-02-10 12:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('alpha_two_code', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/shop/')),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShopBranch',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(max_length=7)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('eta_rang', models.CharField(blank=True, max_length=7, null=True)),
                ('description', models.TextField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Shop Branches',
            },
        ),
        migrations.CreateModel(
            name='ShopType',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='UserBranch',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permission', models.IntegerField(choices=[(0, 'Viewer'), (1, 'Moderator'), (2, 'Editor'), (3, 'Admin')], default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch')),
            ],
            options={
                'verbose_name_plural': 'User Branches',
            },
        ),
    ]
