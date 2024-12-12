from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Student, University
from accounts.utils.base import GenderTextChoies
from django.core.exceptions import ValidationError
import uuid
from datetime import date

class UniversityModelTest(TestCase):
    def setUp(self):
        self.university_data = {
            'name': 'Test University',
            'address': '123 Academic Avenue',
            'established_on': 1990
        }

    def test_create_university(self):
        """Test creating a valid university"""
        university = University.objects.create(**self.university_data)
        self.assertIsNotNone(university.uid)
        self.assertEqual(university.name, 'Test University')
        self.assertEqual(university.established_on, 1990)

    def test_university_str_representation(self):
        """Test string representation of University"""
        university = University.objects.create(**self.university_data)
        self.assertEqual(str(university), 'Test University')

    def test_university_ordering(self):
        """Test university ordering by name"""
        University.objects.create(name='B University', address='Address B', established_on=1985)
        University.objects.create(name='A University', address='Address A', established_on=1980)
        
        universities = list(University.objects.all())
        self.assertEqual(universities[0].name, 'A University')
        self.assertEqual(universities[1].name, 'B University')

class StudentModelTest(TestCase):
    def setUp(self):
        self.university = University.objects.create(
            name='Model Test University',
            address='123 Test Street',
            established_on=1990
        )

    def test_create_student(self):
        """Test creating a valid student"""
        student = Student.objects.create(
            name='Test Student',
            age=22,
            gender=GenderTextChoies.MALE,
            address='456 Student Lane',
            university=self.university,
            enrollment_date=date.today()
        )
        self.assertIsNotNone(student.uid)
        self.assertEqual(student.name, 'Test Student')
        self.assertEqual(student.gender, GenderTextChoies.MALE)

    def test_student_str_representation(self):
        """Test string representation of Student"""
        student = Student.objects.create(
            name='Representation Test',
            age=20,
            gender=GenderTextChoies.FEMALE,
            address='789 Campus Road',
            university=self.university,
            enrollment_date=date.today()
        )
        expected_str = f"Representation Test - {self.university.name} - Female"
        self.assertEqual(str(student), expected_str)

    def test_student_gender_choices(self):
        """Test gender choices"""
        valid_genders = [GenderTextChoies.MALE, GenderTextChoies.FEMALE]
        for gender in valid_genders:
            student = Student.objects.create(
                name=f'Gender {gender} Student',
                age=22,
                gender=gender,
                address='Test Address',
                university=self.university,
                enrollment_date=date.today()
            )
            self.assertEqual(student.gender, gender)

    def test_student_ordering(self):
        """Test student ordering by name"""
        Student.objects.create(
            name='B Student', 
            age=22, 
            gender=GenderTextChoies.MALE,
            address='Address B',
            university=self.university,
            enrollment_date=date.today()
        )
        Student.objects.create(
            name='A Student', 
            age=20, 
            gender=GenderTextChoies.FEMALE,
            address='Address A',
            university=self.university,
            enrollment_date=date.today()
        )
        
        students = list(Student.objects.all())
        self.assertEqual(students[0].name, 'A Student')
        self.assertEqual(students[1].name, 'B Student')

class StudentUniversityAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        # Create a test university
        self.university = University.objects.create(
            name='Test University',
            address='123 Test Street',
            established_on=1990
        )

        # Create a test student
        self.student = Student.objects.create(
            name='John Doe',
            age=22,
            gender=GenderTextChoies.MALE,
            address='456 Student Lane',
            university=self.university,
            enrollment_date=date.today()
        )

    def test_create_student(self):
        data = {
            'name': 'Jane Smith',
            'age': 20,
            'gender': GenderTextChoies.FEMALE,
            'address': '789 Campus Road',
            'university': self.university.uid,
            'enrollment_date': str(date.today())
        }
        response = self.client.post('/api/students/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Jane Smith')
        self.assertEqual(response.data['gender'], GenderTextChoies.FEMALE)

    def test_list_students(self):
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_student_detail(self):
        response = self.client.get(f'/api/students/{self.student.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')
        self.assertEqual(response.data['gender'], GenderTextChoies.MALE)

    def test_create_student_with_invalid_university(self):
        """Test creating a student with non-existent university"""
        invalid_university_uid = uuid.uuid4()
        data = {
            'name': 'Invalid Student',
            'age': 25,
            'gender': GenderTextChoies.MALE,
            'address': '404 Not Found St',
            'university': invalid_university_uid,
            'enrollment_date': str(date.today())
        }
        response = self.client.post('/api/students/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)