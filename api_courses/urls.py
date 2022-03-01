from rest_framework import routers

from api_courses.views import CourseViewSet

app_name = 'api_courses'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'', CourseViewSet, basename='course')

urlpatterns = router.urls
