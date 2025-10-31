from django.urls import path

from testing.schedule import views

urlpatterns = [
    path("schedules/", views.schedule_list, name="schedule_list"),
    path("schedules/<int:pk>/intervals/", views.schedule_intervals_view, name="schedule-intervals-fragment"),
    path("intervals/<int:pk>/delete/", views.delete_interval, name="delete-interval")
]
