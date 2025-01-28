from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    address=serializers.CharField()
    age=serializers.IntegerField()
    mobile_number=serializers.CharField()
    



