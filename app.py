"""App.py concatenates two files."""
from moviepy.editor import *
from moviepy.video.fx.all import resize


"""Variables for the file of the user and the reaction of his friend."""
clip_file = ImageClip("files/file_4N4jqj71s4.jpg")
clip_reaction = ImageClip("files/file_4N4jqj71s4.jpg")

""" I don't know why VideoFileClip it's not working."""
# clip_reaction = VideoFileClip("files/reaction_4N4jqj71s4.jpg", audio=True)


"""Gather both in an array of clips."""
array_of_clips = clips_array([[clip_file], [clip_reaction]])

"""Add images for the specific layout you want to create."""
button = ImageClip("assets/reeact_button_2x.png").set_pos(("right", "bottom")).resize(.85)  # NOQA
top_frame = ImageClip("assets/topbar_2x.png").set_pos(("top")).resize(width=568)  # NOQA

"""Composite the clip with the past vars."""
final_clip = CompositeVideoClip([array_of_clips, button, top_frame]).set_duration(4)  # NOQA


"""Write videoclip."""
final_clip.write_videofile("react.mov", fps=24, audio=True, codec="libx264", audio_codec="pcm_s16le")  # NOQA
