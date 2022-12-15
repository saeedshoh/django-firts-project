from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Rubrik(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("rubrik", kwargs={"pk": self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']
