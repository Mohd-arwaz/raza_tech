# Generated by Django 4.1.5 on 2023-02-12 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arwaz', '0003_student_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='state',
            new_name='city',
        ),
    ]
