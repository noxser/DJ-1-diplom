from django import forms


class TestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {'placeholder': 'Представьтесь', 'class': 'form-control'}),
                           label='Имя')
    description = forms.CharField(widget=forms.Textarea(attrs=
                                                        {'placeholder': 'Содержание', 'rows': '2', 'cols': '60',
                                                         'class': 'form-control'}), label='Содержание')
    radio_mark = forms.TypedChoiceField(
        widget=forms.RadioSelect,
        choices=((1, '1',), (2, '2',), (3, '3',), (4, '4',), (5, '5',))
    )
