from django.test import TestCase
from .models import Enrollment, User, Subject


class SubjectTestCase(TestCase):

    def setUp(self):

        # create courses
        subject1 = Subject.objects.create(sub_id="CN321", sub_name="Data", semester=1, year=2022, seat=1, status="OPEN")
        student1 = User.objects.create_user(username="6310611089", password="P@123456")

    def test_seat_available(self):
        """ is_seat_available should be True """

        subject = Subject.objects.first()
        self.assertTrue(subject.is_seat_available())

    # def test_seat_not_available(self):
    #     """ is_seat_available should be False """

    #     subject = Subject.objects.first()
    #     student = User.objects.first()
    #     Enrollment.objects.create(student_name=student, sub_enroll=subject)

    #     self.assertFalse(subject.is_seat_available())
    

