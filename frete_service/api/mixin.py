from api.controller import FreteController
from api.dtos import FreteDTO
from api.repositories import FreteRepository


class FreteMixin:
    
    frete_controller = FreteController()
    frete_repository = FreteRepository()

    def frete_get_all(self):
        lista_fretes = self.frete_repository.get_all()
        fretes_dto = self.frete_controller.get_lista_fretes_dto(lista_fretes=lista_fretes)
        return [frete.model_dump() for frete in fretes_dto]


    def frete_get_by_uuid(self, uuid: str):
        frete = self.frete_repository.get_by_uuid(uuid=uuid)
        if not frete:
            return None

        frete_dto = self.frete_controller.get_frete_output_dto(frete=frete)
        return frete_dto.model_dump()

    def frete_create(self, frete_dto: FreteDTO):
        return self.frete_repository.create(frete_dto=frete_dto)

    def frete_delete(self, uuid: str):
        return self.frete_repository.delete(uuid=uuid)