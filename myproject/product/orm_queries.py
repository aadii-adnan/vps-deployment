from django.db.models import Count

from .models import Product


def get_product_orm_examples():
    """Return 10 ORM query examples for the Product model."""

    return {
        "1_price_range_100_to_500": Product.objects.filter(price__range=(100, 500)),
        "2_price_greater_than_1000": Product.objects.filter(price__gt=1000),
        "3_price_less_than_or_equal_200": Product.objects.filter(price__lte=200),
        "4_order_by_price_ascending": Product.objects.order_by("price"),
        "5_order_by_price_descending": Product.objects.order_by("-price"),
        "6_exclude_out_of_stock": Product.objects.exclude(stock=0),
        "7_exclude_products_under_50": Product.objects.exclude(price__lt=50),
        "8_total_product_count": Product.objects.count(),
        "9_product_count_per_category": Product.objects.values("category__name").annotate(total=Count("id")).order_by("-total"),
        "10_any_product_exists": Product.objects.exists(),
    }