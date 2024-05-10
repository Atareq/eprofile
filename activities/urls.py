from rest_framework.routers import DefaultRouter

from activities.api import (ClinicViewSet, LectureViewSet,
                            OperationAttendanceViewSet, ShiftAttendanceViewSet)

router = DefaultRouter()

router.register(r'lectures', LectureViewSet)
router.register(r'clinics-attendance', ClinicViewSet)
router.register(r'shifts-attendance', ShiftAttendanceViewSet)
router.register(r'operations-attendance', OperationAttendanceViewSet)


urlpatterns = [
    '', router.urls,
    'studnetactivit/']
