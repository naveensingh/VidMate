from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.fx.resize import resize

from animations.dvd_screen_saver import DVDScreenSaver

screen_saver = DVDScreenSaver(
    size=(1920, 1080),
    clip_size=(320, 180)
)


def create_dvd_screen_saver():
    with VideoFileClip("rc_f16_jet.mp4") as clip:
        clip = clip.fx(resize, width=320)
        size = (1920, 1080)
        video = CompositeVideoClip(
            [clip.set_position(
                lambda t: screen_saver.calculate_position(t)
            ).set_start(0).crossfadein(1)],
            size=size
        )
        video.write_videofile("output.mp4", threads=8, fps=30)
        video.close()
