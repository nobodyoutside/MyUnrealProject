import unreal

@unreal.uclass()
class EditorUtils(unreal.GlobalEditorUtilityBase):
    pass

select_assets = EditorUtils().get_selected_assets()
for asset in select_assets:
    unreal.log("===================")
    unreal.log(asset.get_full_name()) # (class name + full path)
    unreal.log(asset.get_fname())
    unreal.log(asset.get_name())
    unreal.log(asset.get_path_name())
    unreal.log(asset.get_class())
    unreal.log("===================")