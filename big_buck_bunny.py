from moviepy.editor import download_webfile

BIG_BUCK_BUNNY_URL = "https://download.blender.org/demo/movies/BBB/bbb_sunflower_1080p_30fps_normal.mp4"

big_buck_bunny = download_webfile(
    BIG_BUCK_BUNNY_URL,
    filename="big_buck_bunny.mp4",
    overwrite=False
)
