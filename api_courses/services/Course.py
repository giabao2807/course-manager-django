from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from api_account.models import Student
from api_courses.models import CourseStudent
from api_courses.serializers import CourseSerializer


class CourseService:

    @classmethod
    @transaction.atomic
    def create(cls, request):
        course_data = request.data
        serializer = CourseSerializer(data=course_data)

        if serializer.is_valid(raise_exception=True):
            course = serializer.save()

            student_ids = course_data.get("student_ids")
            students = Student.objects.filter(id__in=student_ids)

            if len(students) != len(student_ids):
                raise ValidationError({"error_message": "student_ids is not valid"})

            course_students = []
            for student in students:
                course_students.append(CourseStudent(course=course, student=student))

            CourseStudent.objects.bulk_create(course_students)
            return serializer.data
