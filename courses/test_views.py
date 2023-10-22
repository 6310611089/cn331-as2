from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Course, QuotaRequest

class CourseViewTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            course_id="CN230", 
            course_name="DATABASE SYSTEMS", 
            semester=2, 
            year=2023, 
            seat=20, 
            course_open=True
        )

        self.user = User.objects.create_user(
            username="user1",
            password="user1234"
        )

    def test_register_view_login(self):
        c = Client()
        c.login(username="user1", password="user1234")
        response = c.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_no_login(self):
        c = Client()
        response = c.get(reverse('register'))
        self.assertEqual(response.status_code, 302)

    def test_request_quota_view(self):
        c = Client()
        c.login(username="user1", password="user1234")
        response = c.post(reverse('request_quota', args=[self.course.id]))
        self.assertEqual(response.status_code, 302)

    def test_cancel_request_view(self):
        c = Client()
        c.login(username="user1", password="user1234")
        quota_request = QuotaRequest.objects.create(student=self.user, course=self.course, course_approved=False)
        response = c.post(reverse('cancel_request', args=[quota_request.id]))
        self.assertEqual(response.status_code, 302)