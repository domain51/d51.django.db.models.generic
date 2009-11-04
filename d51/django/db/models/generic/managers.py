from d51.django.db.models.generic.query import GenericRelationshipQuerySet
from django.db import models

class GenericRelationshipManager(models.Manager):
    def return_related(self):
        return self.all().return_related()

    def get_query_set(self):
        return GenericRelationshipQuerySet(self.model)

