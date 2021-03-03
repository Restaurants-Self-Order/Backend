# Generated by Django 3.1.7 on 2021-03-02 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_auto_20210302_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.currency'),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customizationitem',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch'),
        ),
        migrations.AddField(
            model_name='customizationitem',
            name='customization_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.customizationgroup'),
        ),
        migrations.AddField(
            model_name='customizationitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
        migrations.AddField(
            model_name='customizationgroup',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch'),
        ),
        migrations.AlterUniqueTogether(
            name='modifiergroup',
            unique_together={('item', 'customization_group')},
        ),
    ]