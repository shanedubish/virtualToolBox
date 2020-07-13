from rest_framework import serializers

from v_toolbox.models import ToolBox

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBox
        fields = ('name','cost','location','type','image')
