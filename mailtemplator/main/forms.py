from django import forms

class MailForm(forms.Form):
    choices = (
        ('schedule1', 'スケジュール調整（提案）'),
        ('schedule2', 'スケジュール調整（確認）')
    )
    template = forms.ChoiceField(label="テンプレートを使用", choices=choices)
    title = forms.CharField(label="件名")
    content = forms.CharField(label="メール本文", widget=forms.Textarea)
