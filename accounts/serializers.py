from rest_framework import serializers
from .models import Student, University

from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        user_obj = User.objects.create_user(**validated_data)
        return user_obj



class UniversitySerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = ['uid', 'name', 'address', 'ranking', 'established_year', 'students']
    
    def get_students(self, obj):
        return StudentSerializer(Student.objects.filter(university= obj), many=True).data

    def create(self, validated_data):
        return University.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.ranking = validated_data.get('ranking', instance.ranking)
        instance.established_year = validated_data.get('established_year', instance.established_year)
        instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    university_details = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['uid', 'name', 'age', 'gender', 'address', 'university', 'enrollment_date', 'university_details']
        extra_kwargs = {
            'university': {'write_only': True}
        }
    
    def get_university_details(self, obj : Student):
        return {
            'uid': obj.university.uid,
            'name': obj.university.name,
        }

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.address = validated_data.get('address', instance.address)
        instance.enrollment_date = validated_data.get('enrollment_date', instance.enrollment_date)
        instance.university = validated_data.get('university', instance.university)
        instance.save()
        return instance