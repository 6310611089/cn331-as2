from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, QuotaRequest

# Create your tests here.

class CourseModelTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            course_id="CN230", 
            course_name="DATABASE SYSTEMS", 
            semester=2, 
            year=2023, 
            seat=20, 
            course_open=True
        )

    def test_course_model_str(self):
        self.assertEqual(str(self.course), "CN230 (DATABASE SYSTEMS)")

    def test_seat_available(self):
        self.assertTrue(self.course.seat > 0)

    def test_course_open(self):
        self.assertTrue(self.course.course_open)


class QuotaRequestModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="user1",
            password="user1234"
        )

        self.course = Course.objects.create(
            course_id="CN200", 
            course_name="DISCRETE MATHEMATICS", 
            semester=1, 
            year=2023, 
            seat=10, 
            course_open=True
        )

        self.request_quota = QuotaRequest.objects.create(
            student=self.user,
            course=self.course,
            course_approved=False
        )
    
    def test_quota_request_model_str(self):
        request_quota_str = f'{self.request_quota.course}'
        self.assertEqual(str(self.request_quota), request_quota_str)