# Generated by Django 3.1.7 on 2021-03-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modifiergroup',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch'),
        ),
        migrations.AddField(
            model_name='modifiergroup',
            name='customization_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.customizationgroup'),
        ),
        migrations.AddField(
            model_name='modifiergroup',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
        migrations.AddField(
            model_name='item',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopbranch'),
        ),
    ]
