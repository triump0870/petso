from rest_framework import serializers

from pets.models import Pet


class PetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='apis:pet-detail')

    class Meta:
        model = Pet
        fields = ('url', 'name', 'birth_day', 'type')

    def validate(self, attrs):
        print("attr: ", attrs)
        return attrs
