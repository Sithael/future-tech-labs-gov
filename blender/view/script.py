import bpy

class TestPanel(bpy.types.Panel):
   
    bl_label = "Rysuj obiekt"
   
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
   
    bl_category = "Narzedzie Jakuba"
   
    def draw(self, context):
       
        layout = self.layout
       
        row = layout.row()
        row.label(text="Rysuj szescian w 3D")
       
        row = layout.row()
        row.operator("mesh.primitive_monkey_add", text="Dodaj Szescian")
       
def register():
    bpy.utils.register_class(TestPanel)
   
register()
