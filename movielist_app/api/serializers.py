from rest_framework import serializers
from movielist_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):

    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def get_len_name(self, object):
    #     return len(object.name)

    # object level validators
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidaionError(
    #             "Titile and description should be different")
    #     else:
    #         return

    # # field level validators
    # def validate_name(self, value):
    #     if(len(value) < 2):
    #         raise serializers.ValidaionError(
    #             "Name must be at least 2 characters long")
    #     else:
    #         return

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
