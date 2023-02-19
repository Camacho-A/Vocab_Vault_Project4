from .models import Dictionary
from rest_framework import serializers


class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Dictionary
        # Which fields should be included in the output
        fields = ['id', 'word', 'pronunciation',
                  'partOfSpeech', 'definition', 'context']
