# Generated by Django 4.2.5 on 2023-10-05 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppNico', '0002_login_register_delete_entregable_delete_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='email',
            new_name='usuario',
        ),
    ]
