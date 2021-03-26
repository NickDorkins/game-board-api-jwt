from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Rules

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_rules = Rules.objects.create(
            creator = testuser1,
            game = 'Green Eggs and Ham',
            rule_set = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_rules.save()

    def test_blog_content(self):
        rules = Rules.objects.get(id=1)
        actual_creator = str(rules.creator)
        actual_game = str(rules.game)
        actual_rule_set = str(rules.rule_set)
        self.assertEqual(actual_creator, 'testuser1')
        self.assertEqual(actual_game, 'Green Eggs and Ham')
        self.assertEqual(actual_rule_set, 'I do not like green eggs and ham, Sam I  am.')
