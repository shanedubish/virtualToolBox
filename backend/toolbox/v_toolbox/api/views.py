from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView

from v_toolbox.models import ToolBox
from .serializers import ToolSerializer

class ToolsListView(ListAPIView):
    queryset = ToolBox.objects.all()
    serializer_class = ToolSerializer
