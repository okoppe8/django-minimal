from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from pure_pagination.mixins import PaginationMixin

from .filters import ItemFilter
from .forms import ItemForm
from .models import Item


# Create your views here.
# 検索一覧画面
class ItemFilterView(LoginRequiredMixin, PaginationMixin, FilterView):
    model = Item
    filterset_class = ItemFilter
    # デフォルトの並び順を新しい順とする
    queryset = Item.objects.all().order_by('-created_at')

    # pure_pagination用設定
    paginate_by = 10  # 10件/ページ
    object = Item

    # 詳細画面から戻るボタンを押したときに、詳細画面遷移前のページ状態に戻す処理
    def get(self, request, **kwargs):
        # GETクエリーがある（一覧画面での検索実行・ページ移動）なら検索条件を保存
        if request.GET:
            request.session['query'] = request.GET
        # GETクエリーが無い場合（詳細・登録画面より戻るボタン）なら検索条件を復元
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    # 登録者の設定
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')
