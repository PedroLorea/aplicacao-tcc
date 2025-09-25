from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed
from .repositories import AuthenticationRepository


class AuthenticationMixin:
    def __init__(self):
        self.repository = AuthenticationRepository()

    def register_user(self, request, email: str, senha: str):
        if self.repository.get_user_by_email(email):
            raise AuthenticationFailed("Usuário já existe.")
        return self.repository.create_user(email=email, senha=senha)

    def login_user(self, request, email: str, senha: str):
        user = authenticate(request, email=email, password=senha)
        if not user:
            raise AuthenticationFailed("Credenciais inválidas.")
        login(request, user)
        return user

    def logout_user(self, request):
        logout(request)
