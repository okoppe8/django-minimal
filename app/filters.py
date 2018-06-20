from django_filters import filters, FilterSet

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):
    order_by = MyOrderingFilter(

        fields=(
            ('created_by', 'created_by'),
            ('created_at', 'created_at'),
        ),
        field_labels={
            'created_by': '登録者',
            'created_at': '登録日',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = '__all__'
