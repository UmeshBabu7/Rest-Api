from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    address=serializers.CharField()
    age=serializers.IntegerField()
    mobile_number=serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        # Update the fields of the instance
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.age = validated_data.get('age', instance.age)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.save()
        return instance



