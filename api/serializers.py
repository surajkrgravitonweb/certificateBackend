from rest_framework import serializers
from .models import *

from rest_framework import serializers
from .models import Certificate, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('subject', 'marks_obtained', 'minimum_marks', 'maximum_marks')

class CertificateSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, required=False)  # Make it not required if grades can be empty

    class Meta:
        model = Certificate
        fields = ('student_id', 'student_name', 'fathers_name', 'course_duration', 'from_date', 'to_date', 'certificate_issue_date', 'grades')

    def create(self, validated_data):
        grades_data = validated_data.pop('grades', [])  # Handle grades being optional
        certificate = Certificate.objects.create(**validated_data)
        for grade_data in grades_data:
            if grade_data.get('subject'):  # Only create Grade if 'subject' is not empty
                Grade.objects.create(certificate=certificate, **grade_data)
        return certificate



class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['subject', 'marks_obtained', 'minimum_marks', 'maximum_marks']

class CertificateSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = Certificate
        fields = ['student_id', 'student_name', 'fathers_name', 'course_duration', 'from_date', 'to_date', 'certificate_issue_date', 'grades']