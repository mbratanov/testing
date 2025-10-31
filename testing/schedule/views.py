from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from testing.schedule.forms import ScheduleIntervalForm
from testing.schedule.models import Schedule, ScheduleInterval


def schedule_list(request):
    object_list = Schedule.objects.all()
    context = {
        "title": "Schedules",
        "object_list": object_list,
    }

    return render(request, "schedule/index.html", context)


def schedule_intervals_view(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleIntervalForm(request.POST)
        if form.is_valid():
            interval = form.save(commit=False)
            interval.schedule = schedule
            interval.save()
            form = ScheduleIntervalForm()  # изчистване на формата
    else:
        form = ScheduleIntervalForm()
    return render(request, 'partials/schedule_intervals.html', {
        'schedule': schedule,
        'form': form,
    })


@csrf_exempt
def delete_interval(request, pk):
    interval = get_object_or_404(ScheduleInterval, pk=pk)
    schedule_id = interval.schedule.id
    interval.delete()
    return redirect('schedule-intervals-fragment', pk=schedule_id)
