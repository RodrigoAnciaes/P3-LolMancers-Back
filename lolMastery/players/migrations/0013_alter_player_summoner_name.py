# Generated by Django 4.1.1 on 2022-11-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0012_alter_player_saved_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='summoner_name',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
    ]
