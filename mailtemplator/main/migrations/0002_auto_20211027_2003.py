# Generated by Django 3.2.7 on 2021-10-27 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labels',
            options={'verbose_name': 'Label', 'verbose_name_plural': 'Labels'},
        ),
        migrations.AlterModelOptions(
            name='mailaddresses',
            options={'verbose_name': 'MailAddress', 'verbose_name_plural': 'MailAddresses'},
        ),
        migrations.AlterModelOptions(
            name='sampletemplates',
            options={'verbose_name': 'sampletemplate', 'verbose_name_plural': 'sampletemplates'},
        ),
        migrations.AlterModelOptions(
            name='templates',
            options={'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
    ]