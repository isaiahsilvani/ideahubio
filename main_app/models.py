from django.db import models
from django.shortcuts import reverse
from datetime import date, datetime
from django.contrib.auth.models import User
# Create your models here.

INDUSTRIES = (
    ('Advertising','Advertising'),
    ('Aerospace','Aerospace'),
    ('Agriculture','Agriculture'),
    ('Air Transport','Air Transport'),
    ('Alcoholic Beverages','Alcoholic Beverages'),
    ('Alternative Energy','Alternative Energy'),
    ('Architectural Services','Architectural Services'),
    ('Automotive','Automotive'),
    ('Banking','Banking'),
    ('Business Services','Business Services'),
    ('Chemical Manufacturing','Chemical Manufacturing'),
    ('Construction','Construction'),
    ('Credit Unions','Credit Unions'),
    ('Cruise Ships','Cruise Ships'),
    ('Defense','Defense'),
    ('Dentists','Dentists'),
    ('Drug Manufacturers','Drug Manufacturers'),
    ('Education','Education'),
    ('Electric Utilities','Electric Utilities'),
    ('Eletronics Manufacturing','Eletronics Manufacturing'),
    ('Energy & Natural Resources','Energy & Natural Resources'),
    ('Farming','Farming'),
    ('Finance','Finance'),
    ('Food & Beverages','Food & Beverages'),
    ('For-profit Education','For-profit Education'),
    ('Funeral Services','Funeral Services'),
    ('Gambling & Casinos','Gambling & Casinos'),
    ('Gas & Oil','Gas & Oil'),
    ('General Contractors','General Contractors'),
    ('Health Services','Health Services'),
    ('Home Builders','Home Builders'),
    ('Hotels, Motels & Tourism','Hotels, Motels & Tourism'),
    ('Insurance','Insurance'),
    ('Internet','Internet'),
    ('Liquor, Wine & Beer','Liquor, Wine & Beer'),
    ('Logging','Logging'),
    ('Marine Transport','Marine Transport'),
    ('Meat processing & products','Meat processing & products'),
    ('Medical Supplies','Medical Supplies'),
    ('Music Production','Music Production'),
    ('Non-profit Organization','Non-profit Organization'),
    ('Nutritional Supplements','Nutritional Supplements'),
    ('Oil & Gas','Oil & Gas'),
    ('Payday Lenders','Payday Lenders'),
    ('Pharmaceutical Manufacturing','Pharmaceutical Manufacturing'),
    ('Power Utilities','Power Utilities'),
    ('Printing & Publishing','Printing & Publishing'),
    ('Radio/TV Stations','Radio/TV Stations'),
    ('Real Estate','Real Estate'),
    ('Record Label','Record Label'),
    ('Recreation','Recreation'),
    ('Restuarants','Restuarants'),
    ('Retail Sales','Retail Sales'),
    ('Savings & Loans','Savings & Loans'),
    ('Schools/Education','Schools/Education'),
    ('Securities & Investments','Securities & Investments'),
    ('Teachers Unions','Teachers Unions'),
    ('Telecom Services','Telecom Services'),
    ('Tobacco','Tobacco'),
    ('Transportation','Transportation'),
    ('Trucking','Trucking'),
    ('TV Production','TV Production'),
    ('Venture Capital','Venture Capital'),
    ('Other','Other'),
)

class Idea(models.Model):
  name = models.CharField(max_length=70)
  logo_url = models.CharField(default="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/ProhibitionSign2.svg/1200px-ProhibitionSign2.svg.png", max_length=300)
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
    return f"{self.get_industry_display()}"
  
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
  