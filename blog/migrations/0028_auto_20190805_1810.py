# Generated by Django 2.2.3 on 2019-08-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20190719_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('PG-TRB', 'PG-TRB'), ('POLY-TRB', 'POLY-TRB'), ('ENGR-TRB', 'ENGR-TRB'), ('TNSET', 'TNSET'), ('GATE', 'GATE')], max_length=255),
        ),
    ]
