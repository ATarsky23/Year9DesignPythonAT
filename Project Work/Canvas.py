class TargetMakerPanel(bpy.types.Panel) :
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "CrowD"
    def draw(self, context) :
        layout = self.layout
        layout = self.layout
        TheCol = self.layout.row(align = True)
        TheCol.operator("mesh.make_target", text = "Add Target")
        TheCol.prop(context.scene, "Render_Target")
        TheCol = self.layout.row(align = True)
        TheCol.prop(context.scene, "GroupSelection")
        TheCol.operator("render.preset_add", text="", icon='ZOOMIN')
        TheCol.operator("render.preset_add", text="", icon='ZOOMOUT').remove_active = True
        row = layout.row()
        row.prop(context.scene, "Mingle")
        row = layout.row()
        row.prop(context.scene, "People_Name")
        layout.label(text=" Random Speed:")
        row = layout.row()
        row.prop(context.scene, "Min_Speed")
        row.prop(context.scene, "Max_Speed")
        layout.label(text=" Random Spawn minimum:")
        row = layout.row(align=True)
        row.prop(context.scene, "Min_X")
        row.prop(context.scene, "Min_Y")
        row.prop(context.scene, "Min_Z")
        layout.label(text=" Random Spawn maximum:")
        row = layout.row(align=True)
        row.prop(context.scene, "Max_X")
        row.prop(context.scene, "Max_Y")
        row.prop(context.scene, "Max_Z")
        layout.label(text=" Number of people to spawn:")
        row = layout.row(align=True)
        row.prop(context.scene, "SpawnCount")

bpy.types.Scene.Mingle = bpy.props.BoolProperty\
(
    name = "Mingle",
    description = "Decides if people should mingle or not."
    ) 
bpy.types.Scene.Render_Target = bpy.props.BoolProperty\
(
    name = "Render Target",
    default = False,
    description = "Decides if the Target plane should be rendered."
    )       
bpy.types.Scene.Min_Speed= bpy.props.IntProperty\
    (
    name = "MinSpeed",
    default = 1,
    description = "Minimum speed of the people."
    )        
bpy.types.Scene.Max_Speed= bpy.props.IntProperty\
    (
    name = "MaxSpeed",
    default = 1,
    description = "Maximum speed of the people."
    ) 
bpy.types.Scene.Min_X= bpy.props.IntProperty\
    (
    name = "Min X",
    default = 1,
    description = "Minimum X location of the people."
    ) 
bpy.types.Scene.Min_Y= bpy.props.IntProperty\
    (
    name = "Min Y",
    default = 1,
    description = "Minimum Y location of the people."
    ) 
bpy.types.Scene.Min_Z= bpy.props.IntProperty\
    (
    name = "Min Z",
    default = 1,
    description = "Minimum Z location of the people."
    ) 
bpy.types.Scene.Max_X= bpy.props.IntProperty\
    (
    name = "Max X",
    default = 1,
    description = "Maximum X location of the people"
    ) 
bpy.types.Scene.Max_Y= bpy.props.IntProperty\
    (
    name = "Max Y",
    default = 1,
    description = "Maximum Y location of the people"
    ) 
bpy.types.Scene.Max_Z= bpy.props.IntProperty\
    (
    name = "Max Z",
    default = 1,
    description = "Maximum Z location of the people"
    ) 
bpy.types.Scene.People_Name = bpy.props.StringProperty\
    (
    name = "Spawn Names",
    description = "The name the people will be called when spawned"
    )
bpy.types.Scene.SpawnCount= bpy.props.IntProperty\
    (
    name = "Spawn Count",
    default = 10,
    description = "How many people should spawn"
    ) 
bpy.types.Scene.GroupSelection = EnumProperty(
        items = [("1", "Group 1", "First Group"),
                 ("2", "Group 2", "Second Group"),
                 ("3", "Group 3", "Third Group")],
        name = "GroupNumber")


class MakeTarget(bpy.types.Operator) :
    bl_idname = "mesh.make_target"
    bl_label = "Add Target"
    bl_options = {"UNDO"}

    def invoke(self, context, event):

        Vertices = \
          [
            mathutils.Vector((-2, -2,0)),
            mathutils.Vector((2, -2, 0)),
            mathutils.Vector((2, 2, 0)),
            mathutils.Vector((-2, 2, 0)),

          ]
        NewMesh = bpy.data.meshes.new("Target")
        NewMesh.from_pydata \
          (
            Vertices,
            [],
            [[0, 1, 2], [0, 1, 3], [1, 2, 3], [2, 0, 3]]
          )
        NewMesh.update()
        NewObj = bpy.data.objects.new("Target", NewMesh)
        context.scene.objects.link(NewObj)     
        if context.scene.Render_Target == True:
            bpy.data.objects["Target"].hide_render = False
        if context.scene.Render_Target == False:
            bpy.data.objects["Target"].hide_render = True
        return {"FINISHED"}
    #end invoke


def register() :
    bpy.utils.register_class(MakeTarget)
    bpy.utils.register_class(TargetMakerPanel)

def unregister() :
    bpy.utils.unregister_class(MakeTarget)
    bpy.utils.unregister_class(TargetMakerPanel)

if __name__ == "__main__" :
    register()