from .models import Usuario

class AuthenticationRepository:

    def create_user(self, email: str, senha: str) -> Usuario:
        return Usuario.objects.create_user(email=email, password=senha)

    def get_user_by_email(self, email: str) -> Usuario | None:
        return Usuario.objects.filter(email=email).first()
