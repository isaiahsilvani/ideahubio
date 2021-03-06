# Generated by Django 3.2.2 on 2021-05-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_idea_logo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='industry',
            field=models.CharField(choices=[('Advertising', 'Advertising'), ('Aerospace', 'Aerospace'), ('Agriculture', 'Agriculture'), ('Air Transport', 'Air Transport'), ('Alcoholic Beverages', 'Alcoholic Beverages'), ('Alternative Energy', 'Alternative Energy'), ('Architectural Services', 'Architectural Services'), ('Automotive', 'Automotive'), ('Banking', 'Banking'), ('Business Services', 'Business Services'), ('Chemical Manufacturing', 'Chemical Manufacturing'), ('Construction', 'Construction'), ('Credit Unions', 'Credit Unions'), ('Cruise Ships', 'Cruise Ships'), ('Defense', 'Defense'), ('Dentists', 'Dentists'), ('Drug Manufacturers', 'Drug Manufacturers'), ('Education', 'Education'), ('Electric Utilities', 'Electric Utilities'), ('Eletronics Manufacturing', 'Eletronics Manufacturing'), ('Energy & Natural Resources', 'Energy & Natural Resources'), ('Farming', 'Farming'), ('Finance', 'Finance'), ('Food & Beverages', 'Food & Beverages'), ('For-profit Education', 'For-profit Education'), ('Funeral Services', 'Funeral Services'), ('Gambling & Casinos', 'Gambling & Casinos'), ('Gas & Oil', 'Gas & Oil'), ('General Contractors', 'General Contractors'), ('Health Services', 'Health Services'), ('Home Builders', 'Home Builders'), ('Hotels, Motels & Tourism', 'Hotels, Motels & Tourism'), ('Insurance', 'Insurance'), ('Internet', 'Internet'), ('Liquor, Wine & Beer', 'Liquor, Wine & Beer'), ('Logging', 'Logging'), ('Marine Transport', 'Marine Transport'), ('Meat processing & products', 'Meat processing & products'), ('Medical Supplies', 'Medical Supplies'), ('Music Production', 'Music Production'), ('Non-profit Organization', 'Non-profit Organization'), ('Nutritional Supplements', 'Nutritional Supplements'), ('Oil & Gas', 'Oil & Gas'), ('Payday Lenders', 'Payday Lenders'), ('Pharmaceutical Manufacturing', 'Pharmaceutical Manufacturing'), ('Power Utilities', 'Power Utilities'), ('Printing & Publishing', 'Printing & Publishing'), ('Radio/TV Stations', 'Radio/TV Stations'), ('Real Estate', 'Real Estate'), ('Record Label', 'Record Label'), ('Recreation', 'Recreation'), ('Restuarants', 'Restuarants'), ('Retail Sales', 'Retail Sales'), ('Savings & Loans', 'Savings & Loans'), ('Schools/Education', 'Schools/Education'), ('Securities & Investments', 'Securities & Investments'), ('Teachers Unions', 'Teachers Unions'), ('Telecom Services', 'Telecom Services'), ('Tobacco', 'Tobacco'), ('Transportation', 'Transportation'), ('Trucking', 'Trucking'), ('TV Production', 'TV Production'), ('Venture Capital', 'Venture Capital'), ('Other', 'Other')], default=('Advertising', 'Advertising'), max_length=70),
        ),
    ]
