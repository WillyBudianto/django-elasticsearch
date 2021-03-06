# Generated by Django 3.2.8 on 2022-06-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20220630_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterUniqueTogether(
            name='producttypeattribute',
            unique_together={('product_attribute', 'product_type')},
        ),
    ]
