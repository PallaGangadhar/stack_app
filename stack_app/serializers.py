from rest_framework import serializers
from stack_app.models import *


class QuestionsSerializer(serializers.ModelSerializer):
    """ Return questions list """

    class Meta:
        model = Questions
        fields = ["id", "question", "view_count", "answer_count", "score"]
