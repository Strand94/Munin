from django.test import TestCase
from .models import Course
from apps.registration.models import User


#Tests registration
class CourseTestCase(TestCase):
    def setUp(self):
        # Sets up  person who will act as lecturer
        User.objects.create_user(username='Pekka', email='pekka@pekkamail.com', school=None, first_name='Pekka',
                                 middle_name='', last_name='Abrahamson', image='')

        # Sets up a course.
        pekka_course_1 = Course(name = 'Forskningsgymnastikk og Demokrati', course_id = 666, lecturer = User.objects.get(username = 'Pekka'), year = 1950)
        pekka_course_2 = Course(name = 'Matematikk 3B', course_id = 22, lecturer = User.objects.get(username = 'Pekka'), year = 1950)

        pekka_course_1.save()
        pekka_course_2.save()

    # Tests the __str__() function which is supposed to return course_id and name of the course
    def test_person_a(self):
        self.assertEqual(Course.objects.get(course_id = 666).__str__(), '666 - Forskningsgymnastikk og Demokrati')

    def test_person_b(self):
        self.assertEqual(Course.objects.get(course_id = 22).__str__(), '22 - Matematikk 3B')