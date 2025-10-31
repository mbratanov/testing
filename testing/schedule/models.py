from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Schedule(models.Model):
    NAME_MAX_LENGTH = 255

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )


class ScheduleInterval(models.Model):
    HOURS_MIN = 1
    HOURS_MAX = 24
    HOURS_DEFAULT = 0
    MONTH_MIN = 1
    MONTH_MAX = 12
    DAY_MIN = 1
    DAY_MAX = 31

    schedule = models.ForeignKey(
        to=Schedule,
        on_delete=models.CASCADE,
        related_name="intervals",
    )

    start_date_day = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(DAY_MIN),
            MaxValueValidator(DAY_MAX),
        ],
    )

    start_date_month = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MONTH_MIN),
            MaxValueValidator(MONTH_MAX),
        ],
    )

    end_date_day = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(DAY_MIN),
            MaxValueValidator(DAY_MAX),
        ],
    )

    end_date_month = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MONTH_MIN),
            MaxValueValidator(MONTH_MAX),
        ],
    )

    hours_weekdays = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(HOURS_MIN),
            MaxValueValidator(HOURS_MAX),
        ],
        default=HOURS_DEFAULT,
    )
    hours_saturdays = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(HOURS_MIN),
            MaxValueValidator(HOURS_MAX),
        ],
        default=HOURS_DEFAULT,
    )

    hours_sundays = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(HOURS_MIN),
            MaxValueValidator(HOURS_MAX),
        ],
        default=HOURS_DEFAULT,
    )
