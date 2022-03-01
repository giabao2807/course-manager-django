from api_account.constants import RoleData
from api_base.permission import MyBasePermission


class AdminPermission(MyBasePermission):
    match_any_roles = [RoleData.ADMIN]


class LecturePermission(MyBasePermission):
    match_any_roles = [RoleData.LECTURE]


class StudentPermission(MyBasePermission):
    match_any_roles = [RoleData.STUDENT]


class AdminOrLecturPermission(MyBasePermission):
    match_any_roles = [RoleData.ADMIN, RoleData.STUDENT]

