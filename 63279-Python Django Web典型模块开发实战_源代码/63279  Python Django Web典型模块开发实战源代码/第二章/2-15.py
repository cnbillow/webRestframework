class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields="__all__"#��������������ֶζ����л�
        fields = ('title', 'isbn', 'author')  # ָ�����л�ĳЩ�ֶ�
