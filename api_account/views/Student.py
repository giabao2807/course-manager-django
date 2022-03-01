from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.constants import RoleData
from api_account.models import Student
from api_account.permission import StudentPermission
from api_account.serializers import StudentSerializer, StudentRegisterSerializer
from api_account.services import AccountService, StudentService
from api_base.views import BaseViewSet


class StudentViewSet(BaseViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_map = {
        "edit": [StudentPermission]
    }

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        student_data = request.data

        if not student_data.get('account'):
            return Response({"error_message": "account is required!! "}, status=status.HTTP_400_BAD_REQUEST)
        student_data['account']['role'] = RoleData.STUDENT.value['id']
        serializer = StudentRegisterSerializer(data=student_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            token_data = AccountService.login_with_username_password(student_data['account']['username'],
                                                                    student_data['account']['password'],
                                                                    RoleData.STUDENT)

        return Response(token_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'])
    def edit(self, request, *args, **kwargs):
        account = request.user
        avatar = request.FILES.get('avatar')

        student = Student.objects.filter(account=account)
        if not student.exists():
            return {"error_message": "request user is not valid"}
        student = student.first()
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if avatar:
                url = StudentService.upload_avatar(avatar)
                account.avatar = url
                account.save()
            return Response(serializer.data)
