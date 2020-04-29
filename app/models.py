from django.contrib.auth.models import User
from django.db import models


class EventType(models.Model):
    """
    Describes the types of events that can exist in the system. This is
    customizable with some sane defaults.

    Initial values are loaded from app.fixtures.yaml when the application starts.
    They can be either changed in the yaml file or updated via the admin UI.

    Note that due to the way that fixtures work, you cannot edit things that have
    been loaded via fixture in the admin UI. However, things added in the admin UI
    will not be removed when fixtures are re-added.

    #TODO make items added via fixtures uneditable
    """
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class RelationshipType(models.Model):
    """
    Describes the types of relationships that can exist between
    a user of rolorex and a human. This is customizable with sane
    defaults.

    Uses Fixtures similar to EventType
    #TODO make items added via fixtures uneditable
    """
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Human(models.Model):
    """
    Humans exists in the world and have a M:M relationship with
    Users of rolorex.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    users = models.ManyToManyField(User, through='Relationship')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Relationship(models.Model):
    """
    Relationship models the relationship that a user of
    rolorex has with a Human.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)
    type = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)
    established = models.IntegerField(null=True, blank=True)
