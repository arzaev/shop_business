# Generated by Django 3.2.5 on 2021-07-08 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_article_subcategory_productsubcategory_subcategory_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsubcategory',
            old_name='article_category',
            new_name='category_name',
        ),
    ]
