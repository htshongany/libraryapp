# Generated by Django 4.1.7 on 2023-04-27 02:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=4000, null=True),
        ),
    ]
