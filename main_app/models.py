from django.db import models
from django.shortcuts import reverse
from datetime import date, datetime
from django.contrib.auth.models import User
# Create your models here.

INDUSTRIES = (
    ('0','Advertising'),
    ('1','Aerospace'),
    ('2','Agriculture'),
    ('3','Air Transport'),
    ('4','Alcoholic Beverages'),
    ('5','Alternative Energy'),
    ('6','Architectural Services'),
    ('7','Automotive'),
    ('8','Banking'),
    ('9','Business Services'),
    ('10','Chemical Manufacturing'),
    ('11','Construction'),
    ('12','Credit Unions'),
    ('13','Cruise Ships'),
    ('14','Defense'),
    ('15','Dentists'),
    ('16','Drug Manufacturers'),
    ('17','Education'),
    ('18','Electric Utilities'),
    ('19','Eletronics Manufacturing'),
    ('20','Energy & Natural Resources'),
    ('21','Farming'),
    ('22','Finance'),
    ('23','Food & Beverages'),
    ('24','For-profit Education'),
    ('25','Funeral Services'),
    ('26','Gambling & Casinos'),
    ('27','Gas & Oil'),
    ('28','General Contractors'),
    ('29','Health Services'),
    ('30','Home Builders'),
    ('31','Hotels, Motels & Tourism'),
    ('32','Insurance'),
    ('33','Internet'),
    ('34','Liquor, Wine & Beer'),
    ('35','Logging'),
    ('36','Marijuana'),
    ('37','Marine Transport'),
    ('38','Meat processing & products'),
    ('39','Medical Supplies'),
    ('40','Music Production'),
    ('41','Non-profit Organization'),
    ('42','Nutritional Supplements'),
    ('43','Oil & Gas'),
    ('44','Payday Lenders'),
    ('45','Pharmaceutical Manufacturing'),
    ('46','Power Utilities'),
    ('47','Printing & Publishing'),
    ('48','Radio/TV Stations'),
    ('49','Real Estate'),
    ('50','Record Label'),
    ('51','Recreation'),
    ('52','Restuarants'),
    ('53','Retail Sales'),
    ('54','Savings & Loans'),
    ('55','Schools/Education'),
    ('56','Securities & Investments'),
    ('57','Teachers Unions'),
    ('58','Telecom Services'),
    ('59','Tobacco'),
    ('60','Transportation'),
    ('61','Trucking'),
    ('62','TV Production'),
    ('63','Venture Capital'),
    ('64','Other'),
)

class Idea(models.Model):
  name = models.CharField(max_length=70)
  logo_url = models.CharField(max_length=300)
  description = models.CharField(max_length=10000)
  is_public = models.BooleanField(default=False)
  people_interested = models.CharField(max_length=100)
  date = models.DateTimeField(default=datetime.now, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  industry = models.CharField(
    max_length = 70,
    choices=INDUSTRIES,
    default=INDUSTRIES[0]
  )

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("detail", kwargs={"idea_id": self.id})

class Employee(models.Model):
  role = models.CharField(max_length=80)
  auth_level = models.IntegerField()
  function = models.CharField(max_length=250)
  idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

  def __str__(self):
    return f"Employee for idea_id {self.idea_id}"
  

# class Industry(models.Model):
#   industry = models.CharField(
#     max_length = 70,
#     choices=INDUSTRIES,
#     default=INDUSTRIES[len(INDUSTRIES) - 1]
#   )
#   idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

  # def __str__(self):
  #   return f"The industry is {self.get_industry_display()} for idea_id: {self.idea_id}"

class Photo(models.Model):
  url = models.CharField(max_length=200)
  idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for idea_id {self.idea_id} @ {self.url}"
  