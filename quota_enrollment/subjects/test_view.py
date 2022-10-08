from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import Subject, Enrollment, User


class SubjectViewTestCase(TestCase):

    def setUp(self):
        subject1 = Subject.objects.create(sub_id="CN321", sub_name="Data", semester=1, year=2022, seat=1, status="OPEN")
        student1 = User.objects.create_user(username="6310611089", password="P@123456")

    def test_index_view_status_code(self):
        """ index view's status code is ok """

        c = Client()
        response = c.get(reverse('subjects:index'))
        self.assertEqual(response.status_code, 200)

    def test_valid_login_page(self):
        """ valid flight page should return status code 200 """

        c = Client()
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 302)