from rest_framework.serializers import ModelSerializer
from user_operations.models import Apply


class ApplySerializer(ModelSerializer):

    class Meta:
        model = Apply
        fields = '__all__'

