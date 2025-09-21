from typing import List
from api.dtos import FreteDTO
from api.models import Frete


class FreteController:
    
    def get_frete_output_dto(self, frete: Frete):

        dto = FreteDTO(
            id=frete.id,
            produto=frete.produto
        )

        return dto
    

    def get_lista_fretes_dto(self, lista_fretes: List[Frete]):
        lista_fretes_dto = [self.get_frete_output_dto(frete) for frete in lista_fretes]

        return lista_fretes_dto
