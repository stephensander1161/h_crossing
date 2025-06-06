import unreal

ISLAND_MAP_PATH = '/Game/TropicalIsland'
ISLAND_MAP_NAME = 'TropicalIsland'

# Asset references from StarterContent
PLANE_ASSET = '/Game/StarterContent/Shapes/Shape_Plane.Shape_Plane'
CONE_ASSET = '/Game/StarterContent/Shapes/Shape_Cone.Shape_Cone'
GRASS_MATERIAL = '/Game/StarterContent/Materials/M_Ground_Grass.M_Ground_Grass'
WATER_MATERIAL = '/Game/StarterContent/Materials/M_Water_Ocean.M_Water_Ocean'
ROCK_MATERIAL = '/Game/StarterContent/Materials/M_Rock_Sandstone.M_Rock_Sandstone'


def create_island_level():
    # Ensure destination folder exists
    if not unreal.EditorAssetLibrary.does_directory_exist(ISLAND_MAP_PATH):
        unreal.EditorAssetLibrary.make_directory(ISLAND_MAP_PATH)

    # Create blank map and save it
    world = unreal.EditorLoadingAndSavingUtils.new_blank_map(False)
    unreal.EditorLoadingAndSavingUtils.save_current_level_as(f"{ISLAND_MAP_PATH}/{ISLAND_MAP_NAME}")

    # Spawn island plane
    plane = unreal.load_asset(PLANE_ASSET)
    island_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(plane, unreal.Vector(0.0, 0.0, 0.0))
    island_actor.set_actor_scale3d(unreal.Vector(50.0, 50.0, 1.0))
    island_comp = island_actor.static_mesh_component
    grass = unreal.load_asset(GRASS_MATERIAL)
    island_comp.set_material(0, grass)

    # Spawn surrounding ocean
    ocean_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(plane, unreal.Vector(0.0, 0.0, -10.0))
    ocean_actor.set_actor_scale3d(unreal.Vector(500.0, 500.0, 1.0))
    ocean_comp = ocean_actor.static_mesh_component
    water = unreal.load_asset(WATER_MATERIAL)
    ocean_comp.set_material(0, water)

    # Spawn volcano using cone mesh
    cone = unreal.load_asset(CONE_ASSET)
    volcano_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(cone, unreal.Vector(0.0, 0.0, 10.0))
    volcano_actor.set_actor_scale3d(unreal.Vector(20.0, 20.0, 20.0))
    volcano_comp = volcano_actor.static_mesh_component
    rock = unreal.load_asset(ROCK_MATERIAL)
    volcano_comp.set_material(0, rock)

    # Save final level
    unreal.EditorLoadingAndSavingUtils.save_current_level()


if __name__ == '__main__':
    create_island_level()
