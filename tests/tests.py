from django.utils import timezone
from django.test import TestCase
from tests.models import (
    Yearly, Montly, CustomFormat,
    Child1Parent1, Child2Parent1,
    Child1Parent2, Child2Parent2,
    Child1Parent3, Child2Parent3
)


class TestNumeratedModel(TestCase):

    def test_yearly_reset_autonumber_concistency(self):
        created_at = timezone.datetime(2019, 1, 31, 0, 0, 0)
        obj1 = Yearly(name='year', created_at=created_at)
        obj1.save()
        self.assertEqual(obj1.inner_id, '1901000%s' % obj1.reg_number)
        obj1.delete()

        obj2 = Yearly(name='year', created_at=created_at)
        obj2.save()
        self.assertEqual(obj2.inner_id, '1901000%s' % obj2.reg_number)

        created_at = timezone.datetime(2020, 1, 31, 0, 0, 0)
        obj3 = Yearly(name='year', created_at=created_at)
        obj3.save()
        self.assertEqual(obj3.inner_id, '2001000%s' % obj3.reg_number)

    def test_montly_reset_autonumber_concistency(self):
        created_at = timezone.datetime(2019, 1, 1, 0, 0, 0)
        obj1 = Montly(name='month', created_at=created_at)
        obj1.save()
        self.assertEqual(obj1.inner_id, '1901000%s' % obj1.reg_number)
        obj1.delete()

        obj2 = Montly(name='month', created_at=created_at)
        obj2.save()
        self.assertEqual(obj2.inner_id, '1901000%s' % obj2.reg_number)

        created_at = timezone.datetime(2019, 2, 1, 0, 0, 0)
        obj3 = Montly(name='month', created_at=created_at)
        obj3.save()
        self.assertEqual(obj3.inner_id, '1902000%s' % obj3.reg_number)

    def test_custom_doc_prefix(self):
        created_at = timezone.datetime(2019, 1, 1, 0, 0, 0)
        obj = CustomFormat(name='CS', created_at=created_at)
        obj.save()
        self.assertEqual(obj.inner_id, 'CS1901000%s' % obj.reg_number)

    def test_doc_prefix_in_polymorphic_child_model(self):
        created_at = timezone.datetime(2019, 1, 1, 0, 0, 0)
        child_1 = Child1Parent1(name='Child1', created_at=created_at)
        child_1.save()
        self.assertEqual(child_1.inner_id, 'C11901000%s' % child_1.reg_number)

        child_2 = Child2Parent1(name='Child2', created_at=created_at)
        child_2.save()
        self.assertEqual(child_2.inner_id, 'C21901000%s' % child_2.reg_number)

    def test_doc_prefix_in_polymorphic_parent_model(self):
        created_at = timezone.datetime(2019, 1, 1, 0, 0, 0)
        child_1 = Child1Parent2(name='Child1', created_at=created_at)
        child_1.save()
        self.assertEqual(child_1.inner_id, 'P21901000%s' % child_1.reg_number)

        child_2 = Child2Parent2(name='Child2', created_at=created_at)
        child_2.save()
        self.assertEqual(child_2.inner_id, 'P21901000%s' % child_2.reg_number)

    def test_numerator_mixin_in_polymorphic_child_model(self):
        created_at = timezone.datetime(2019, 1, 1, 0, 0, 0)
        child_1 = Child1Parent3(name='Child1', created_at=created_at)
        child_1.save()
        self.assertEqual(child_1.inner_id, 'C11901000%s' % child_1.reg_number)

        child_2 = Child2Parent3(name='Child2', created_at=created_at)
        child_2.save()
        self.assertEqual(child_2.inner_id, 'C21901000%s' % child_2.reg_number)
