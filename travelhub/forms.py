from django import forms
from .models import Tag, Comment

class PostSearchForm(forms.Form):
    """記事検索フォーム。"""
    key_word = forms.CharField(
        label='検索キーワード',
        required=False,
    )

    tags = forms.ModelMultipleChoiceField(
        label='タグでの絞り込み',
        required=False,
        queryset=Tag.objects.order_by('name'),
    )