# Generated by Django 4.2.1 on 2023-06-23 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_review_communication_bool_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='problem_sol',
            new_name='problem_solving',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='problem_bool',
            new_name='problem_solving_bool',
        ),
    ]
