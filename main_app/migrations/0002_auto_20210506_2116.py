# Generated by Django 3.2.2 on 2021-05-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='industry',
            field=models.CharField(choices=[('0', 'Advertising'), ('1', 'Aerospace'), ('2', 'Agriculture'), ('3', 'Air Transport'), ('4', 'Alcoholic Beverages'), ('5', 'Alternative Energy'), ('6', 'Architectural Services'), ('7', 'Automotive'), ('8', 'Banking'), ('9', 'Business Services'), ('10', 'Chemical Manufacturing'), ('11', 'Construction'), ('12', 'Credit Unions'), ('13', 'Cruise Ships'), ('14', 'Defense'), ('15', 'Dentists'), ('16', 'Drug Manufacturers'), ('17', 'Education'), ('18', 'Electric Utilities'), ('19', 'Eletronics Manufacturing'), ('20', 'Energy & Natural Resources'), ('21', 'Farming'), ('22', 'Finance'), ('23', 'Food & Beverages'), ('24', 'For-profit Education'), ('25', 'Funeral Services'), ('26', 'Gambling & Casinos'), ('27', 'Gas & Oil'), ('28', 'General Contractors'), ('29', 'Health Services'), ('30', 'Home Builders'), ('31', 'Hotels, Motels & Tourism'), ('32', 'Insurance'), ('33', 'Internet'), ('34', 'Liquor, Wine & Beer'), ('35', 'Logging'), ('36', 'Marijuana'), ('37', 'Marine Transport'), ('38', 'Meat processing & products'), ('39', 'Medical Supplies'), ('40', 'Music Production'), ('41', 'Non-profit Organization'), ('42', 'Nutritional Supplements'), ('43', 'Oil & Gas'), ('44', 'Payday Lenders'), ('45', 'Pharmaceutical Manufacturing'), ('46', 'Power Utilities'), ('47', 'Printing & Publishing'), ('48', 'Radio/TV Stations'), ('49', 'Real Estate'), ('50', 'Record Label'), ('51', 'Recreation'), ('52', 'Restuarants'), ('53', 'Retail Sales'), ('54', 'Savings & Loans'), ('55', 'Schools/Education'), ('56', 'Securities & Investments'), ('57', 'Teachers Unions'), ('58', 'Telecom Services'), ('59', 'Tobacco'), ('60', 'Transportation'), ('61', 'Trucking'), ('62', 'TV Production'), ('63', 'Venture Capital'), ('64', 'Other')], default=('64', 'Other'), max_length=70),
        ),
        migrations.DeleteModel(
            name='INDUSTRY',
        ),
    ]
