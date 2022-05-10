from django.db import models

# Create your models here.
class BiographyM(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    description = models.CharField(max_length=200,null=True)
    source = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class AnimalM(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    description = models.CharField(max_length=200,null=True)
    source = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class VeganismM(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    description = models.CharField(max_length=200,null=True)
    source = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class ImmigrantM(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    description = models.CharField(max_length=200,null=True)
    source = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class FamilyM(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    description = models.CharField(max_length=200,null=True)
    source = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name