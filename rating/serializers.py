from rest_framework import serializers
from rating.models import Review, ReviewImages


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImages
        fields = '__all__'


class ReviewActionSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=False, required=False)
    owner = serializers.ReadOnlyField(source='owner.email')
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Review
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['images'] = ReviewImageSerializer(instance.images.all(), many=True).data
        return repr


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, attrs):
        request = self.context['request']
        product = attrs['product']
        user = request.user
        if user.reviews.filter(product=product).exists():
            raise serializers.ValidationError('You already reviewed this product!')
        return attrs


class ReviewUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Review
        fields = '__all__'
