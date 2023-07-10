# Generated by Django 4.2.3 on 2023-07-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='category',
            field=models.CharField(choices=[('AN', 'Animals'), ('BU', 'Business'), ('CO', 'Community'), ('CR', 'Creative'), ('ED', 'Education'), ('EM', 'Emergencies'), ('EN', 'Environment'), ('EV', 'Events'), ('FA', 'Faith'), ('FM', 'Family'), ('FN', 'Funeral & Memorial'), ('MD', 'Medical'), ('MB', 'Monthly Bills'), ('NW', 'Newlyweds'), ('OT', 'Other'), ('SP', 'Sports'), ('TR', 'Travel'), ('UR', 'Ukraine Relief'), ('VO', 'Volunteer'), ('WI', 'Wishes')], default='OT', max_length=2),
        ),
        migrations.AddField(
            model_name='campaign',
            name='web3_raised_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]