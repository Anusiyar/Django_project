from django.db import models

# Create your models here.

class slider(models.Model):
    name = models.CharField(max_length=200, blank = False)
    profession = models.CharField(max_length=200, blank = False)
    description = models.TextField()
    introtitle = models.CharField(max_length=200, blank = False)
    introdescription = models.TextField()
    img = models.ImageField(upload_to = 'slider', null = True)

    def __str__(self):
        return self.name

class whatido(models.Model):
    title = models.CharField(max_length=200, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.title

class whatidoitem(models.Model):
    title = models.CharField(max_length=200, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.title

class about(models.Model):
    title = models.CharField(max_length=200, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.title

class aboutbrief(models.Model):
    title = models.CharField(max_length=200, blank = False)
    description = models.TextField()
    img = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

class aboutprojects(models.Model):
    title = models.CharField(max_length=200, blank = False)
    counts = models.IntegerField(blank = False)
    def __str__(self):
        return self.title

class aboutskill(models.Model):
    title = models.CharField(max_length=200, blank = False)
    counts = models.IntegerField(blank = False)
    def __str__(self):
        return self.title

class work(models.Model):
    title = models.CharField(max_length=200, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.title

class workimg(models.Model):
    name = models.CharField(max_length=200, blank = False)
    img = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name

class experience(models.Model):
    title = models.CharField(max_length=200, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.title

class experiencelist(models.Model):
    title = models.CharField(max_length=200, blank = False)
    year = models.CharField(max_length=200, blank = False, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class contacttitle(models.Model):
    title = models.CharField(max_length=200, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.title

class contactaddr(models.Model):
    addr = models.CharField(max_length=200, blank = False)
    mail = models.CharField(max_length=200, blank = False)
    phone = models.CharField(max_length=200, blank = False)

    def __str__(self):
        return self.mail

class contactform(models.Model):
    name = models.CharField(max_length=200, blank = False)
    mail = models.CharField(max_length=200, blank = False)
    phone = models.CharField(max_length=200, blank = False)
    messages = models.TextField()

    def __str__(self):
        return self.mail



