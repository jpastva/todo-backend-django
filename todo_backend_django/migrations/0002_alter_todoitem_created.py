# Generated by Django 3.2.5 on 2021-07-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_backend_django', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
