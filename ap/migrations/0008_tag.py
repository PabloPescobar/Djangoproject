# Generated by Django 4.2.3 on 2023-08-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0007_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]



    
   