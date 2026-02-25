from django import forms


class AdminSetupForm(forms.Form):
    employee_number = forms.CharField(
        max_length=50,
        label='従業員番号',
        widget=forms.TextInput(attrs={
            'placeholder': '従業員番号を入力',
            'autocomplete': 'off',
        }),
    )
    password = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'パスワードを入力',
        }),
    )
    password_confirm = forms.CharField(
        label='パスワード（確認）',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'パスワードを再入力',
        }),
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('パスワードが一致しません。')

        return cleaned_data
