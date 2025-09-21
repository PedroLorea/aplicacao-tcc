
from api.models import Frete
from api.dtos import FreteDTO

class FreteRepository:
    def get_all(self):
        return Frete.objects.all()
    
    def get_by_uuid(self, uuid: str):
        return Frete.objects.filter(uuid=uuid).first() # Retorna None se não existir
    
    def create(self, frete_dto: FreteDTO):

        frete = Frete(**frete_dto.dict())
        frete.save()
        return frete

        # defaults = {
        #     "produto": frete_dto.produto
        # }

        # frete, created = Frete.objects.update_or_create(frete_dto.id, defaults=defaults)

        # return frete, created

    def delete(self, uuid: str):
        frete = self.get_by_uuid(uuid=uuid)
        if frete:
            frete.delete()
            return True
        return False