from .dtos import LoginInputDTO


class AutorizacaoController:
        
    def get_login_input_dto(
            self,
            data: dict,
        ) -> LoginInputDTO:

            dto = LoginInputDTO(
                email=data["email"].replace(" ", ""),
                senha=str(data["senha"]),
            )
            return dto