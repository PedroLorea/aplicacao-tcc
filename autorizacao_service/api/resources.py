from rest_framework.response import Response
from rest_framework import status

from .controllers import AutorizacaoController

from .autorizacao_api_view import AutorizacaoAPIView

from .dtos import LoginInputDTO
from .mixins import AuthenticationMixin
from rest_framework.permissions import IsAuthenticated



class RegisterView(AutorizacaoAPIView, AuthenticationMixin):
    def post(self, request):
        email = request.data.get("email")
        senha = request.data.get("senha")
        user = self.register_user(request, email, senha)
        return Response({"message": "Usuário criado com sucesso!", "email": user.email}, status=status.HTTP_201_CREATED)


class LoginView(AutorizacaoAPIView, AuthenticationMixin):

    autorizacao_controller = AutorizacaoController()
    input_dto = LoginInputDTO

    def post(self, request):

        print("entrou")
        self.validate_dto(data=request.data)
        input_dto = self.autorizacao_controller.get_login_input_dto(data=request.data)
        print("input_dto: ", input_dto)

        user = self.login_user(request, input_dto.email, input_dto.password)
        return Response({"message": "Login efetuado com sucesso!", "email": user.email})


class LogoutView(AutorizacaoAPIView, AuthenticationMixin):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.logout_user(request)
        return Response({"message": "Logout efetuado com sucesso!"})
