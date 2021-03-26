from django.db import models
from django.contrib.auth import get_user_model


class Rules(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    game = models.CharField(max_length=64)
    rule_set = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game
