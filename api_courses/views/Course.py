from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api_account.permission import AdminPermission
from api_base.views import BaseViewSet
from api_courses.models import Course
from api_courses.serializers import CourseSerializer, ListCourseSerializer
from api_courses.services import CourseService


class CourseViewSet(BaseViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AdminPermission]

    serializer_map = {
        "list": ListCourseSerializer
    }

    def create(self, request, *args, **kwargs):
        res_data = CourseService.create(request)
        return Response(res_data)
