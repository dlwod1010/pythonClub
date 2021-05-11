from django.test import TestCase
from .models import meeting, meetingMinutes, resource, event
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
