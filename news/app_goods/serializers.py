from app_goods.models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'birthday']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'release', 'pages', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author_instance =Author.objects.create(name=author_data['name'], surname=author_data['surname'], birthday=author_data['birthday'])
        book_instance = Book.objects.create(**validated_data, author=author_instance)
        return book_instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.release = validated_data.get('release', instance.release)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.save()
        return instance


'''
class BookSerializer(serializers.HyperlinkedModelSerializer):
    #name = AuthorSerializer(source='author')
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'release', 'pages', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        book = Book.objects.create(**validated_data)
        Author.objects.create(book=book, **author_data)
        return book


'''
'''
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.CharField()

    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        tag = validated_data.pop('tags')
        tag_instance, created = Tag.objects.get_or_create(name=tag)
        article_instance = Article.objects.create(**validated_data, tags=tag_instance)
        return article_instance
'''