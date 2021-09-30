from rest_framework import serializers

from books_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['title']:
            if data['title'][0].islower():
                raise serializers.ValidationError('Title must start with a capital letter!')
        return data

    class Meta:
        model = Book
        fields = '__all__'