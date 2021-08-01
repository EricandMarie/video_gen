import os
import moviepy.video.io.ImageSequenceClip

image_folder = 'images'
fps = 25

image_files = [image_folder + '/' + img for img in os.listdir(image_folder) if img.endswith(".jpg")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('my_video.mp4')
