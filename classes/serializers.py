from rest_framework import serializers
from .models import Class, Series, Modality


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'

    def validate(self, data):
        level = data.get('level')
        period = data.get('period')

        if level is not None and period is not None:
            level_and_period = Series.objects.filter(level=level, period=period)

            if self.instance:
                level_and_period = level_and_period.exclude(pk=self.instance.pk)

            if level_and_period.exists():
                raise serializers.ValidationError("Já existe uma série cadastrada com o mesmo turno")

        return data


class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = '__all__'

    def validate_name(self, value):
        if Modality.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Já existe um campo com esta modalidade")
        return value
