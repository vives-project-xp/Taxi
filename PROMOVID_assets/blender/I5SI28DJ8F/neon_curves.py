# OpenShot Video Editor is a program that creates, modifies, and edits video files.
#   Copyright (C) 2009  Jonathan Thomas
#
# This file is part of OpenShot Video Editor (http://launchpad.net/openshot/).
#
# OpenShot Video Editor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenShot Video Editor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenShot Video Editor.  If not, see <http://www.gnu.org/licenses/>.


# Import Blender's python API.  This only works when the script is being
# run from the context of Blender.  Blender contains it's own version of Python
# with this library pre-installed.
import bpy
import json


def load_font(font_path):
    """ Load a new TTF font into Blender, and return the font object """
    # get the original list of fonts (before we add a new one)
    original_fonts = bpy.data.fonts.keys()

    # load new font
    bpy.ops.font.open(filepath=font_path)

    # get the new list of fonts (after we added a new one)
    for font_name in bpy.data.fonts.keys():
        if font_name not in original_fonts:
            return bpy.data.fonts[font_name]

    # no new font was added
    return None

# Debug Info:
# ./blender -b test.blend -P demo.py
# -b = background mode
# -P = run a Python script within the context of the project file


# Init all of the variables needed by this script.  Because Blender executes
# this script, OpenShot will inject a dictionary of the required parameters
# before this script is executed.
params = {
    'title': 'Oh Yeah! OpenShot!',
    'extrude': 0.1,
    'bevel_depth': 0.02,
    'spacemode': 'CENTER',
    'text_size': 1.5,
    'width': 1.0,
    'fontname': 'Bfont',

    'color': [0.8, 0.8, 0.8],
    'alpha': 1.0,

    'line1_diffuse_color': [0.8, 0.8, 0.8, 1.0],
    'line2_diffuse_color': [0.8, 0.8, 0.8, 1.0],
    'line3_diffuse_color': [0.8, 0.8, 0.8, 1.0],
    'line4_diffuse_color': [0.8, 0.8, 0.8, 1.0],

    'output_path': '/tmp/',
    'fps': 24,
    'quality': 90,
    'file_format': 'PNG',
    'color_mode': 'RGBA',
    'horizon_color': [0.57, 0.57, 0.57],
    'resolution_x': 1920,
    'resolution_y': 1080,
    'resolution_percentage': 100,
    'start_frame': 20,
    'end_frame': 25,
    'animation': True,
}


#BEGIN INJECTING PARAMS
params_json = r"""{"file_name": "Title", "title": "PROJECT EXPERIENCE I.0", "extrude": 0.1, "bevel_depth": 0.02, "fontname": "Bfont", "spacemode": "CENTER", "text_size": 1.0, "width": 1.0, "diffuse_color": [1.0, 0.6705882352941176, 0.0, 1.0], "specular_color": [0.0, 0.7411764705882353, 1.0], "specular_intensity": 0.5, "start_frame": 1, "end_frame": 250, "length_multiplier": 1.0, "depart_title": "New York", "depart_lat_dir": "N", "depart_lat_deg": 39.930000000000014, "depart_lat_min": 42.0, "depart_lat_sec": 51.0, "depart_lon_dir": "W", "depart_lon_deg": 39.93, "depart_lon_min": 0.0, "depart_lon_sec": 23.0, "arrive_title": "Paris", "arrive_lat_dir": "N", "arrive_lat_deg": 39.98, "arrive_lat_min": 42.0, "arrive_lat_sec": 51.0, "arrive_lon_dir": "E", "arrive_lon_deg": 2.0, "arrive_lon_min": 20.86999999999998, "arrive_lon_sec": 7.0, "map_texture": "", "thickness": 0.01, "project_files1": "D:\\Video pE\\IMG_1911.MOV|1080|1920|video|29.97002997002997", "project_files2": "D:\\Video pE\\IMG_1930.MOV|1080|1920|video|29.97002997002997", "project_files3": "D:\\Video pE\\IMG_1937.MOV|1080|1920|video|29.97002997002997", "project_files4": "D:\\Video pE\\IMG_1911.MOV|1080|1920|video|29.97002997002997", "strength": 1.0, "glare_type": "GHOSTS", "line1_diffuse_color": [0.403921568627451, 0.7372549019607844, 1.0, 1.0], "line2_diffuse_color": [0.0, 0.4117647058823529, 1.0, 1.0], "line3_diffuse_color": [0.5098039215686274, 0.7294117647058823, 1.0, 1.0], "line4_diffuse_color": [1.0, 0.8666666666666667, 0.0, 1.0], "fps": 30, "resolution_x": 1280, "resolution_y": 720, "resolution_percentage": 100, "quality": 100, "file_format": "PNG", "color_mode": "RGBA", "alpha_mode": 1, "horizon_color": [0.57, 0.57, 0.57], "animation": true, "output_path": "D:\\Vives\\Fase 1\\Semester 2\\Project experience 1.0\\Github rep\\Fake-Taxi\\PROMOVID_assets\\blender\\I5SI28DJ8F\\Title"}"""
#END INJECTING PARAMS


# The remainder of this script will modify the current Blender .blend project
# file, and adjust the settings.  The .blend file is specified in the XML file
# that defines this template in OpenShot.
# ----------------------------------------------------------------------------

# Process parameters supplied as JSON serialization
try:
    injected_params = json.loads(params_json)
    params.update(injected_params)
except NameError:
    pass

# Modify Text / Curve settings
text_object = bpy.data.curves["Text.001"]
text_object.extrude = params["extrude"]
text_object.bevel_depth = params["bevel_depth"]
text_object.body = params["title"]
text_object.align_x = params["spacemode"]
text_object.size = params["text_size"]
text_object.space_character = params["width"]

# Get font object
font = None
if params["fontname"] != "Bfont":
    # Add font so it's available to Blender
    font = load_font(params["fontname"])
else:
    # Get default font
    font = bpy.data.fonts["Bfont"]

text_object.font = font

# Change the material settings (color, alpha, etc...)
material_object = bpy.data.materials["Material.title"]
material_object.diffuse_color = params["diffuse_color"]
material_object.node_tree.nodes[1].inputs[0].default_value = params["diffuse_color"]
material_object.node_tree.nodes[1].inputs[1].default_value = params["strength"]

# Change line colors
material_object = bpy.data.materials["Material.line1"]
material_object.node_tree.nodes[1].inputs[0].default_value = params["line1_diffuse_color"]

material_object = bpy.data.materials["Material.line2"]
material_object.node_tree.nodes[1].inputs[0].default_value = params["line2_diffuse_color"]

material_object = bpy.data.materials["Material.line3"]
material_object.node_tree.nodes[1].inputs[0].default_value = params["line3_diffuse_color"]

material_object = bpy.data.materials["Material.line4"]
material_object.node_tree.nodes[1].inputs[0].default_value = params["line4_diffuse_color"]

# Change glare type
bpy.data.scenes[0].node_tree.nodes["Glare"].glare_type = params["glare_type"]

# Set the render options.  It is important that these are set
# to the same values as the current OpenShot project.  These
# params are automatically set by OpenShot
bpy.context.scene.render.filepath = params["output_path"]
bpy.context.scene.render.fps = params["fps"]
if "fps_base" in params:
    bpy.context.scene.render.fps_base = params["fps_base"]
bpy.context.scene.render.image_settings.file_format = params["file_format"]
bpy.context.scene.render.image_settings.color_mode = params["color_mode"]
bpy.context.scene.render.film_transparent = params["alpha_mode"]
bpy.context.scene.render.resolution_x = params["resolution_x"]
bpy.context.scene.render.resolution_y = params["resolution_y"]
bpy.context.scene.render.resolution_percentage = params["resolution_percentage"]

# Animation Speed (use Blender's time remapping to slow or speed up animation)
length_multiplier = round(params["length_multiplier"])  # time remapping multiplier
new_length = params["end_frame"] * length_multiplier  # new length (in frames)
bpy.context.scene.render.frame_map_old = 1
bpy.context.scene.render.frame_map_new = length_multiplier

# Set render length/position
bpy.context.scene.frame_start = params["start_frame"]
bpy.context.scene.frame_end = new_length
