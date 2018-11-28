from django.contrib.auth import get_user_model


class EmailAuthBackend(object):
    """
    Аутентификация используя e-mail.
    используем get_user_model для случаев
    с переопределенной моделью пользователя
    """

    def __init__(self):
        self.CurUserModel = get_user_model()

    def authenticate(self, username=None, password=None):
        try:
            user = self.CurUserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except self.CurUserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.CurUserModel.objects.get(pk=user_id)
        except self.CurUserModel.DoesNotExist:
            return None
