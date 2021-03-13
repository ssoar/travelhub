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

class CommentCreateForm(forms.ModelForm):
    """コメント投稿フォーム"""

    class Meta:
        model = Comment
        exclude = ('target', 'created_at')
        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': 'マークダウンに対応しています。\n\n```python\nprint("コードはこのような感じで書く")\n```\n\n[リンクテキスト](https://narito.ninja/)\n\n![画像alt](画像URL)'}
            )
        }