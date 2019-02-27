# Generated by Django 2.1.5 on 2019-02-26 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercompany',
            name='company_name',
        ),
        migrations.AlterField(
            model_name='visitors',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Company', verbose_name='company_ID'),
        ),
    ]