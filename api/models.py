from django.db import models
from datetime import date


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=50)

    x1 = models.FloatField()
    x2 = models.FloatField()
    x3 = models.FloatField()
    x4 = models.FloatField()

    y1 = models.FloatField()
    y2 = models.FloatField()
    y3 = models.FloatField()
    y4 = models.FloatField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.room_name)


class Door(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, null=True)
    x = models.FloatField()
    y = models.FloatField()


class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    room = models.ForeignKey(Room, null=True)
    time = models.DateTimeField(null=True)

    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    z = models.IntegerField(null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.name)


class Human(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.OneToOneField(Entity, null=False)
    gender = models.CharField(max_length=1, null=True)
    operator = models.BooleanField(default=False)

    # def __str__(self):
    #     """
    #     String for representing the Model object (in Admin site etc.)
    #     """
    #     return (self.entity.name)

class AccessPoint(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    room = models.ForeignKey(Room, null=True)
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    z = models.IntegerField(null=True)

class Object(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.OneToOneField(Entity, null=True)
    access_point = models.ForeignKey(AccessPoint, null=True)
    categorie = models.CharField(max_length=60, null=True)
    probabilty = models.IntegerField(null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.entity.name)
