# Generated by Django 2.1.5 on 2019-02-24 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20190224_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='company_id',
            new_name='company',
        ),
    ]