from django.db import models

class GenericRelationshipQuerySet(models.query.QuerySet):
    _return_related = False

    def _clone(self, *args, **kwargs):
        c = super(self.__class__, self)._clone(*args, **kwargs)
        c._return_related = self._return_related
        return c

    def return_related(self, do=True):
        clone = self._clone()
        clone._return_related = True
        return clone

    def __getitem__(self, k):
        item = super(self.__class__, self).__getitem__(k)
        if self._return_related and isinstance(item, ScheduledItem):
            return item.content_object
        return item

