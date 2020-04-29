from django.contrib.auth.models import User
from django.test import TestCase

from app.models import EventType, RelationshipType, Human, Relationship


def _get_field_meta(model, field):
    """
    Helper function to get metadata for field of a given model

    This is used to test assumptions about our model.

    This function assumes that a model
    already exists before it is called.

    :param model: Model with field
    :param field: field from model to get meta for
    :return: metadata object about a field
    """
    obj = model.objects.first()
    return obj._meta.get_field(field)


class EventTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        EventType.objects.create(
            title='Generic Event Type',
            description='Generic Event Type Description'
        )

    def test_title_meta(self):
        obj = _get_field_meta(EventType, 'title')
        self.assertEqual(obj.verbose_name, 'title')
        self.assertEqual(obj.max_length, 255)

    def test_description_label(self):
        event_type = EventType.objects.first()
        field_label = event_type._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_string_representation(self):
        event_type = EventType.objects.first()
        self.assertEqual(str(event_type), event_type.title)


class RelationshipTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        RelationshipType.objects.create(
            label='New Relationship'
        )

    def test_label_props(self):
        obj = _get_field_meta(RelationshipType, 'label')
        self.assertEqual(obj.verbose_name, 'label')
        self.assertEqual(obj.max_length, 50)

    def test_string_representation(self):
        relationship_type = RelationshipType.objects.first()
        self.assertEqual(str(relationship_type), relationship_type.label)


class HumanModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Human.objects.create(
            first_name='Test',
            last_name='Tester',
            dob='1970-01-01'
        )

    def test_first_name_props(self):
        obj = _get_field_meta(Human, 'first_name')
        self.assertEqual(obj.verbose_name, 'first name')
        self.assertEqual(obj.max_length, 255)

    def test_last_name_props(self):
        obj = _get_field_meta(Human, 'last_name')
        self.assertEqual(obj.verbose_name, 'last name')
        self.assertEqual(obj.max_length, 255)

    def test_dob_props(self):
        obj = _get_field_meta(Human, 'dob')
        self.assertEqual(obj.verbose_name, 'dob')
        self.assertTrue(obj.null)
        self.assertTrue(obj.blank)

    def test_string_representation(self):
        human = Human.objects.first()
        expected_name = f'{human.first_name} {human.last_name}'
        self.assertEqual(expected_name, str(human))


class RelationshipModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(
            username='Test',
            password='Tester',
            email='test@tester.com'
        )
        h = Human.objects.create(
            first_name='Test',
            last_name='Tester'
        )
        t = RelationshipType.objects.create(label='New Relationship')
        Relationship.objects.create(
            user=u,
            human=h,
            type=t,
            established=1999
        )

    def test_established_meta(self):
        r = Relationship.objects.first()
        obj = _get_field_meta(Relationship, 'established')
        self.assertTrue(obj.null)
        self.assertTrue(obj.blank)
        self.assertTrue(r.established, 1999)
