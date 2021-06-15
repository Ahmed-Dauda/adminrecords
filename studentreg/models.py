from django.db import models

# Create your models here.

class Salat(models.Model):

    lavel_choices = [
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3')
       
    ]

    term_choices = [
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third')
      
       
    ]

    week_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
      
       
    ]

    attitudes_choices = [
        ('Salat', 'Salat'),
        ('Dining', 'Dining'),
        ('Light Out', 'Light Out'),
        ('Hygiene', 'Hygiene'),
        ('Dress Code', 'Dress Code'),
        ('Prep Class', 'Prep Class'),
        ('Admin/Students', 'Admin/Students '),

       
    ]

    names = models.CharField(max_length=255, null=True, blank=True)
    lavel = models.CharField(choices= lavel_choices, max_length=255, null=True, blank=True)
    term = models.CharField(choices= term_choices, max_length=255, null=True, blank=True)
    week = models.CharField(choices= week_choices, max_length=255, null=True, blank=True)
    attitudes = models.CharField(choices= attitudes_choices, max_length=255, null=True, blank=True)
    monday = models.PositiveIntegerField(default = 14 , null=True, blank=True)
    tuesday = models.PositiveIntegerField(default = 14 ,  null=True, blank=True)
    wednesday = models.PositiveIntegerField(default = 14, null=True, blank=True)
    thursday = models.PositiveIntegerField(default = 14 ,  null=True, blank=True)
    friday = models.PositiveIntegerField(default = 14, null=True, blank=True)
    saturday = models.PositiveIntegerField(default = 15, null=True, blank=True)
    sunday = models.PositiveIntegerField(default = 15, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
    #primarykey = models.PositiveIntegerField(default = 15, null=True, blank=True)
      
     
    def __str__(self):
       return f'{self.names} {self.lavel} {self.term}{self.week} {self.attitudes} {self.monday} {self.tuesday} {self.wednesday} {self.friday} {self.saturday} {self.sunday}'


class Dining(models.Model):

    lavel_choices = [
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3')
       
    ]

    term_choices = [
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD')
      
       
    ]

    week_choices = [
        ('WEEK1', 'WEEK1'),
        ('WEEK2', 'WEEK2'),
        ('WEEK3', 'WEEK3')
      
       
    ]

    dining_choices = [
        ('TIMELY', 'TIMELY'),
        ('ORDERLINESS', 'ORDERLINESS'),
        ('CALMNESS', 'CALMNESS'),
        ('PARKING OF PLATES', 'MAGRIB'),
        ('ALLERGY', 'ALLERGY')
      
       
    ]

    names = models.CharField(max_length=255, null=True, blank=True)
    lavel = models.CharField(choices= lavel_choices, max_length=255, null=True, blank=True)
    term = models.CharField(choices= term_choices, max_length=255, null=True, blank=True)
    week = models.CharField(choices= week_choices, max_length=255, null=True, blank=True)
    dining = models.CharField(choices= dining_choices, max_length=255, null=True, blank=True)
    monday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    tuesday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    wednesday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    thursday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    friday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    saturday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    sunday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
      
     
    def __str__(self):
       return f'{self.names}'

class Lightout(models.Model):

    lavel_choices = [
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3')
       
    ]

    term_choices = [
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD')
      
       
    ]

    week_choices = [
        ('WEEK1', 'WEEK1'),
        ('WEEK2', 'WEEK2'),
        ('WEEK3', 'WEEK3')
      
       
    ]

    lightout_choices = [
        ('TIMELY', 'TIMELY'),
        ('OBEDIENT', 'OBEDIENT'),
        ('QUITNESSS', 'QUITNESS'),
        ('SWICH OF LIGHT', 'SWICH OF LIGHT'),
        
      
       
    ]

    names = models.CharField(max_length=255, null=True, blank=True)
    lavel = models.CharField(choices= lavel_choices, max_length=255, null=True, blank=True)
    term = models.CharField(choices= term_choices, max_length=255, null=True, blank=True)
    week = models.CharField(choices= week_choices, max_length=255, null=True, blank=True)
    lightout = models.CharField(choices= lightout_choices, max_length=255, null=True, blank=True)
    monday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    tuesday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    wednesday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    thursday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    friday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    saturday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    sunday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
      
     
    def __str__(self):
       return f'{self.names}'

class Prep(models.Model):

    lavel_choices = [
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3')
       
    ]

    term_choices = [
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD')
      
       
    ]

    week_choices = [
        ('WEEK1', 'WEEK1'),
        ('WEEK2', 'WEEK2'),
        ('WEEK3', 'WEEK3')
      
       
    ]

    support_choices = [
        ('TIME IN/OUT', 'TIME IN/OUT'),
        ('CALMNESS', 'CALMNESS'),
        ('READING/NOTE COPYING/ ASSIGN', 'READING/NOTE COPYING/ ASSIGN'),
        ('ATTENDANCE', 'ATTENDANCE'),
        
      
       
    ]

    names = models.CharField(max_length=255, null=True, blank=True)
    lavel = models.CharField(choices= lavel_choices, max_length=255, null=True, blank=True)
    term = models.CharField(choices= term_choices, max_length=255, null=True, blank=True)
    week = models.CharField(choices= week_choices, max_length=255, null=True, blank=True)
    prep = models.CharField(choices= support_choices, max_length=255, null=True, blank=True)
    monday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    tuesday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    wednesday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    thursday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    friday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    saturday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    sunday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
      
     
    def __str__(self):
       return f'{self.names}'


class Hygiene(models.Model):

    lavel_choices = [
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3')
       
    ]

    term_choices = [
        ('FIRST', 'FIRST'),
        ('SECOND', 'SECOND'),
        ('THIRD', 'THIRD')
      
       
    ]

    week_choices = [
        ('WEEK1', 'WEEK1'),
        ('WEEK2', 'WEEK2'),
        ('WEEK3', 'WEEK3')
      
       
    ]

    hygiene_choices = [
        ('TIME IN/OUT', 'TIME IN/OUT'),
        ('CALMNESS', 'CALMNESS'),
        ('READING/NOTE COPYING/ ASSIGN', 'READING/NOTE COPYING/ ASSIGN'),
        ('ATTENDANCE', 'ATTENDANCE'),
        
      
       
    ]

    names = models.CharField(max_length=255, null=True, blank=True)
    lavel = models.CharField(choices= lavel_choices, max_length=255, null=True, blank=True)
    term = models.CharField(choices= term_choices, max_length=255, null=True, blank=True)
    week = models.CharField(choices= week_choices, max_length=255, null=True, blank=True)
    hygiene = models.CharField(choices= hygiene_choices, max_length=255, null=True, blank=True)
    monday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    tuesday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    wednesday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    thursday = models.PositiveIntegerField(default = 0 ,  null=True, blank=True)
    friday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    saturday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    sunday = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
      
     
    def __str__(self):
       return f'{self.names}'