from  rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializa un campo para probar nuesto APIView"""
    name = serializers.CharField(max_length=10)
    
