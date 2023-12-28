from django.db import models
from django.utils import timezone


# Main Content Section.
class MainContent(models.Model):
    Main_Title = models.CharField(max_length=200, null=True, blank=True)
    Second_Content = models.CharField(max_length=200, null=True, blank=True)
    Third_Content = models.CharField(max_length=200, null=True, blank=True)

    Date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    Time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    Total_Hours = models.IntegerField(null=True, blank=True)
    Why = models.CharField(max_length=200, null=True, blank=True)
    Dedicated = models.CharField(max_length=200, null=True, blank=True)
    Usefull = models.CharField(max_length=200, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
            self.modified_at = timezone.now()
            super().save(*args, **kwargs)


# Docter Details Section.
class DocterDetails(models.Model):
     Doctor_Profile_Pic = models.ImageField(upload_to='Profile_Pic', null=True, blank=True)
     Doctor_name = models.CharField(max_length=200, null=True, blank=True)
     Doctor_Speciality = models.CharField(max_length=200, null=True, blank=True)
     Total_Franchise = models.CharField(max_length=200, null=True, blank=True)
     Doctor_Panel = models.CharField(max_length=200, null=True, blank=True)
     Cured_Patient = models.CharField(max_length=200, null=True, blank=True)
     Doctor_Experience = models.CharField(max_length=200, null=True, blank=True)
     About_registration = models.CharField(max_length=500, null=True, blank=True)
     Doctor_Pic = models.ImageField(upload_to='Hint_Pic', null=True, blank=True)
     Register_Button = models.CharField(max_length=200, null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
     modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

     def save(self, *args, **kwargs):
            self.modified_at = timezone.now()
            super().save(*args, **kwargs)

     
# Awarded By Section.
class Awarded_By(models.Model):
      Awarded_Img = models.ImageField(upload_to='Award_Img', null=True, blank=True)


# Framework_Steps  Section.
class Framework_Steps(models.Model):
    Image = models.ImageField(upload_to='Framework_Steps_img', null=True, blank=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    Content = models.TextField(null=True, blank=True)
    


# How_Will_This Section.
class How_Will_This(models.Model):
     Heading = models.CharField(max_length=200, null=True, blank=True)
     Content = models.TextField(null=True, blank=True)
     Image = models.ImageField(upload_to='How_Will_This_img', null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
     modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

     def save(self, *args, **kwargs):
            self.modified_at = timezone.now()
            super().save(*args, **kwargs)



# Get_Bonuses Section.
class Get_Bonuses(models.Model):
    Image = models.ImageField(upload_to='Get_Bonuses_img', null=True, blank=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    Content = models.CharField(max_length=200, null=True, blank=True)
    Value = models.CharField(max_length=100, null=True, blank=True)

    


# Who_Attend Section.
class Who_Attend(models.Model):
     Image = models.ImageField(upload_to='Who_Attend_img', null=True, blank=True)
     Who_Attend = models.CharField(max_length=200, null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
     modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

     def save(self, *args, **kwargs):
            self.modified_at = timezone.now()
            super().save(*args, **kwargs)



# How_Does_This Section.
class How_Does_This(models.Model):
     Title = models.CharField(max_length=200, null=True, blank=True)
     Content = models.CharField(max_length=200, null=True, blank=True)
     Point_1 = models.CharField(max_length=200, null=True, blank=True)
     Point_2 = models.CharField(max_length=200, null=True, blank=True)
     Point_3 = models.CharField(max_length=200, null=True, blank=True)
     Point_4 = models.CharField(max_length=200, null=True, blank=True)
     Content_in_Detail = models.CharField(max_length=200, null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
     modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

     def save(self, *args, **kwargs):
            self.modified_at = timezone.now()
            super().save(*args, **kwargs)


# About_Your_Health_Coach Section.
class About_Your_Health_Coach(models.Model):
     Image = models.ImageField(upload_to='Health_Coach_img', null=True, blank=True) 
     Title = models.CharField(max_length=300, null=True, blank=True)
     Name = models.CharField(max_length=200, null=True, blank=True)
     Doctor_Speciality = models.CharField(max_length=200, null=True, blank=True)
     Total_Franchise = models.CharField(max_length=200, null=True, blank=True)
     Details_in_brif = models.CharField(max_length=400, null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
     modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

     def save(self, *args, **kwargs):
            self.modified_at = timezone.now()
            super().save(*args, **kwargs)


# Your_Health_Coach_Awarded Section.
class Your_Health_Coach_Awarded(models.Model):
     Awarded_Img = models.ImageField(upload_to='Award_Img', null=True, blank=True)

    

# FAQs Section.
class FAQs(models.Model):
    Question  = models.CharField(max_length=2000, null=True, blank=True)
    Answer = models.CharField(max_length=2000, null=True, blank=True)

     

# RegistrationForm Section.
class RegistrationForm(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
