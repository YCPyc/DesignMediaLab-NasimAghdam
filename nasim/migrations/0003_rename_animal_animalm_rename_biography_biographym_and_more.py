# Generated by Django 4.0.4 on 2022-05-10 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nasim', '0002_animal_family_immigrant_veganism_remove_biography_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Animal',
            new_name='AnimalM',
        ),
        migrations.RenameModel(
            old_name='Biography',
            new_name='BiographyM',
        ),
        migrations.RenameModel(
            old_name='Family',
            new_name='FamilyM',
        ),
        migrations.RenameModel(
            old_name='Immigrant',
            new_name='ImmigrantM',
        ),
        migrations.RenameModel(
            old_name='Veganism',
            new_name='VeganismM',
        ),
    ]
