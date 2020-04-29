from django.contrib import admin

from app.models import EventType, RelationshipType, Relationship, Human

admin.site.register(EventType)
admin.site.register(RelationshipType)
admin.site.register(Relationship)
admin.site.register(Human)
