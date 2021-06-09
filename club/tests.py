from django.test import TestCase
from .models import meeting, meetingMinutes, resource, event
from django.urls import reverse, reverse_lazy
from .forms import meetingForm
from django.contrib.auth.models import User
from .views import index, getmeetings
# Create your tests here.


class meetingTest(TestCase):
    def test_string(self):
        meetingtest = meeting(meetingTitle='Javascript')
        self.assertEqual(str(meetingtest), meetingtest.meetingTitle)

    def test_table(self):
        self.assertEqual(str(meeting._meta.db_table), 'meeting')


class minuteTest(TestCase):
    def test_string(self):
        minutetest = meetingMinutes(minutesText='minutes text')
        self.assertEqual(str(minutetest), minutetest.minutesText)

    def test_table(self):
        self.assertEqual(str(meetingMinutes._meta.db_table), 'meetingMinute')


class resourceTest(TestCase):
    def test_string(self):
        resourcetest = resource(resourceName='node.js express')
        self.assertEqual(str(resourcetest), resourcetest.resourceName)

    def test_table(self):
        self.assertEqual(str(resource._meta.db_table), 'resource')


class eventTest(TestCase):
    def test_string(self):
        eventtest = event(eventTitle='Celebrate the graduation')
        self.assertEqual(str(eventtest), eventtest.eventTitle)

    def test_table(self):
        self.assertEqual(str(event._meta.db_table), 'event')


class meetingFormTest(TestCase):
    def meetingFormIsValid(self):
        form = meetingForm(data={
            'meetingTitle': "title",
            'meetingDate': "01/01/2021",
            'meetingLocationAt': "JJ building",
            'meetingAgenda': "agenda"})
        self.assertTrue(form.is_valid())


class Authentification_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser1', password='P@ssw0rd1')
        self.meeting = meeting.objects.create(
            meetingTitle='Javascript',
            meetingDate='2021-01-02',
            meetingLocationAt='JJ building',
            meetingAgenda='agenda')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(
            response, '/accounts/login/?next=/club/newmeeting/')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='P@ssw0rd1')
        response = self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/newmeeting.html')


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class GetMeetingsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meeting'))
        self.assertEqual(response.status_code, 200)
