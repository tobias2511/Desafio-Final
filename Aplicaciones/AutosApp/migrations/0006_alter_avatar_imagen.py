# Generated by Django 4.0.5 on 2022-07-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutosApp', '0005_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null='((|R|Rf|RF|u|Fr|Br|U|FR|f|rF|RB|r|F|br|BR|rB|bR|rf|fr|rb|fR|B|b|Rb)\'\'\'|(|R|Rf|RF|u|Fr|Br|U|FR|f|rF|RB|r|F|br|BR|rB|bR|rf|fr|rb|fR|B|b|Rb)""")', upload_to='avatar/'),
        ),
    ]