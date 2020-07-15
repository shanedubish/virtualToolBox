from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView

from v_toolbox.models import ToolBox
from .serializers import ToolSerializer

class ToolsListView(ListAPIView):
    queryset = ToolBox.objects.all()
    serializer_class = ToolSerializer



class ToolsGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = ToolBox.objects.all()
    serializer_class = ToolSerializer

class ToolsCreate(CreateAPIView):
    queryset = ToolBox.objects.all()
    serializer_class = ToolSerializer
