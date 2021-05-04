from rest_framework import serializers

from .models import Publications
from .models import PublicationImages

class PublicationImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicationImages
        fields = ('id', 'image')

class PublicationSerializer(serializers.ModelSerializer):
    post_images = PublicationImagesSerializer(many=True, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Publications
        fields = ('id', 'owner', 'text', 'date', 'post_image', 'owner_nickname', 'owner_avatar')

    def create(self, validated_data):
        user = self.context.get('request').user
        publication = Publications.objects.create(**validated_data)
        images = self.context.get('request').data.getlist('post_image')
        for item in images:
            PublicationImages.objects.create(image=True, publication=publication)
        return publication

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        images = self.context.get('request').data.getlist('post_image')
        if images:
            PublicationImages.objects.filter(publication=instance).delete()
            images_list = [PublicationImages(image=item, publication=instance) for item in images]
            PublicationImages.objects.bulk_create(images_list)
        return instance