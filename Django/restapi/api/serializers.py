from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    roll=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    subject=serializers.CharField(max_length=40)
    age=serializers.IntegerField()
    
    def create(self, validated_data):
       return Student.objects.create(** validated_data)
   
    def update(self, instance, validated_data):
        instance.roll= validated_data.get('roll',instance.roll)
        instance.name= validated_data.get('name',instance.name)
        instance.subject= validated_data.get('subject',instance.subject)
        instance.age= validated_data.get('age',instance.age)
        instance.save()
        return  instance