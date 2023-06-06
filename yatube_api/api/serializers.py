from djoser.serializers import UserSerializer
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id",
                  "text",
                  "pub_date",
                  "author",
                  "image",
                  "group",
                  "comments")


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        read_only=False,
        slug_field='username'
    )

    def validate(self, data):
        user = self.context['request'].user
        follower = data['following']
        if user == follower:
            raise serializers.ValidationError(
                'На самого себя подписываться нельзя'
            )
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Такая подписка уже существует'
            )

        ]
