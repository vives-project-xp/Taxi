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
params_json = r"""{"file_name": "PE", "title1": "Titel 1", "extrude": 0.1, "bevel_depth": 0.02, "fontname": "Bfont", "text_size": 1.0, "start_x": -2.4, "start_z": 0.6, "width": 1.0, "diffuse_color": [0.4980392156862745, 0.4980392156862745, 0.4980392156862745, 1.0], "specular_color": [1.0, 1.0, 1.0], "specular_intensity": 0.5, "diffuse_color_bg": [0.8745098039215686, 0.8627450980392157, 0.9058823529411765, 1.0], "specular_color_bg": [1.0, 1.0, 1.0], "specular_intensity_bg": 0.5, "alpha_bg": 0.733, "start_frame": 1, "end_frame": 80, "length_multiplier": 1.0, "title": "TAXI", "spacemode": "CENTER", "use_alpha": "Yes", "particle_number": 100.0, "ground_on_off": "1", "project_files1": "D:\\Video pE\\IMG_1911.MOV|1080|1920|video|29.97002997002997", "project_files2": "D:\\Video pE\\IMG_1911.MOV|1080|1920|video|29.97002997002997", "project_files3": "D:\\Video pE\\IMG_1911.MOV|1080|1920|video|29.97002997002997", "project_files4": "D:\\Video pE\\IMG_1911.MOV|1080|1920|video|29.97002997002997", "title2": "Titel 2", "title3": "Titel 3", "shadeless": "No", "diffuse_color_t1": [0.0, 0.5450980392156862, 0.9058823529411765, 1.0], "diffuse_color_t2": [0.9058823529411765, 0.0, 0.7529411764705882, 1.0], "diffuse_color_t3": [0.9529411764705882, 0.6784313725490196, 0.0, 1.0], "diffuse_color_t4": [0.0, 0.0, 0.0, 1.0], "fps": 30, "resolution_x": 1280, "resolution_y": 720, "resolution_percentage": 100, "quality": 100, "file_format": "PNG", "color_mode": "RGBA", "alpha_mode": 1, "horizon_color": [0.57, 0.57, 0.57], "animation": true, "output_path": "D:\\Vives\\Fase 1\\Semester 2\\Project experience 1.0\\Github rep\\Fake-Taxi\\PROMOVID_assets\\blender\\P15ZZLTKEE\\PE"}"""
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
#print (bpy.data.curves.keys())
text_object = bpy.data.curves["txtName1"]
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

# set the font
text_object.font = font

# Change the material settings (color, alpha, etc...)
material_object = bpy.data.materials["Material.001"]
material_object.diffuse_color = params["diffuse_color"]
material_object.specular_color = params["specular_color"]
material_object.specular_intensity = params["specular_intensity"]

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
bpy.data.worlds[0].color = params["horizon_color"]
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
