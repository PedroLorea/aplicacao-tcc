
from api.models import Frete

class FreteRepository:
    def get_all(self):
        return Frete.objects.all()
    
    def get_by_id(self, id: int):
        return Frete.objects.filter(id=id).first() # Retorna None se não existir
    
    def create(self, frete: Frete):
        frete.save()
        return frete

    def delete(self, id: int):
        frete = self.get_by_id(id=id)
        if frete:
            frete.delete()
            return True
        return False