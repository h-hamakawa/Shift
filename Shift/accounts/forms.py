from django import forms


class AdminSetupForm(forms.Form):
    """
    初回管理者セットアップフォーム

    管理者の従業員番号とパスワードを入力させるフォーム。
    パスワードは確認用に2回入力し、一致を検証する。

    ModelFormを使わない理由:
        パスワードをハッシュ化してから保存する必要があるため、
        ビュー側でmake_passwordを使って手動で保存処理を行う。

    Fields:
        employee_number: 従業員番号（自由入力、最大50文字）
        password: パスワード（伏せ字入力）
        password_confirm: パスワード確認（伏せ字入力、passwordと一致する必要がある）
    """

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
        """
        パスワードと確認用パスワードの一致を検証する。

        両方のフィールドが入力済みで、かつ値が異なる場合にValidationErrorを発生させる。
        片方が未入力の場合は各フィールドのrequiredバリデーションに任せる。
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('パスワードが一致しません。')

        return cleaned_data
