from rest_framework import serializers
from .models import Time, Place, Schedule


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def validate(self, data):

        existing_schedules = Schedule.objects.filter(date=data['date'], times__in=data['times'])

        if 'id' in self.initial_data:
            existing_schedules = existing_schedules.exclude(id=self.initial_data['id'])

        if existing_schedules.exists():
            raise serializers.ValidationError(
                {'alert_message': ['Já existe um agendamento para a mesma data e horários.']})

        return data

