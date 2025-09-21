from rest_framework.response import Response
from api.base.frete_api_view import FreteAPIView
from api.dtos import FreteDTO
from api.mixin import FreteMixin


class FreteListView(FreteAPIView, FreteMixin):

    def get(self, request):
        fretes = self.frete_get_all()

        return Response(data=fretes)
    
class FreteDetailView(FreteAPIView, FreteMixin):

    def get(self, request, uuid: str):
        frete = self.frete_get_by_uuid(uuid=uuid)
        return Response(data=frete)

class FreteCreateView(FreteAPIView, FreteMixin):

    input_dto = FreteDTO

    def post(self, request):
        frete_dto = self.validate_dto(request.data)
        frete, created = self.frete_create(frete_dto=frete_dto)

        return Response(data={"message": "Frete criado com sucesso", "id": frete.id, "created": created}, status=201)


class FreteDeleteView(FreteAPIView, FreteMixin):

    def delete(self, request, uuid: str):
        
        deleted = self.frete_delete(uuid=uuid)

        if deleted:
            return Response(data={"message": "Frete deletado com sucesso", "id": uuid})
        else:
            return Response(data={"message": "Frete não encontrado", "id": uuid})
            