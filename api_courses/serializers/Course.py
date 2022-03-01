import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api_account.serializers import SimpleLectureSerializer
from api_courses.models import Course, CourseStudent


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate_start_date(self, start_date):
        if start_date.date() <= datetime.datetime.now().date():
            raise ValidationError({"detail": "Start date must greater than date"})
        return start_date

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')

        if start_date >= end_date:
            raise ValidationError({"detail": "End date must greater than start date"})

        return attrs


class ListCourseSerializer(serializers.ModelSerializer):
    # lecture = SimpleLectureSerializer()
    # students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        depth = 1

    # def get_students(self, obj):
    #     return obj.course_students.all().count()