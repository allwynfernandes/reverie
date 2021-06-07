import moviepy.editor as mpy
import datetime

# for docs: https://github.com/Zulko/moviepy/blob/master/moviepy/video/VideoClip.py ; https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html

# camVidSize = 120 # height in pixels
useSubClip = True
def make_montage(camVidSize, outputVideoFrameRate, useSubClip):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M")
    print(now)
    scrClip = mpy.ImageSequenceClip("./data/scr/", fps=outputVideoFrameRate)
    camClip = mpy.ImageSequenceClip("./data/cam/", fps=outputVideoFrameRate)
    camClip = camClip.resize(height=camVidSize)  #.fx(vfx.resize, width = 280) import moviepy.video.fx.all as vfx
    # CAMWIDTH, CAMHEIGHT = camClip.size # Not being used atm
    # SCRWIDTH, SCRHEIGHT = scrClip.size # Not being used atm
    com = mpy.CompositeVideoClip([scrClip, camClip.set_position(("right", "bottom"))])

    # Add audio
    audioClip = mpy.AudioFileClip("./data/snd/audiobinger_sunday_service.mp3")
    if useSubClip:
        audioClip = audioClip.subclip(audioClip.duration-com.duration)
    com = com.set_audio(audioClip)

    scrClip.write_videofile(f"./data/output/Screen_recording_{now}.mp4", preset="ultrafast", threads=3) # high quality
    com.write_videofile(f"./data/output/Movie_{now}.mp4", preset="ultrafast", threads=3) # high quality


def main():
    make_montage(camVidSize, outputVideoFrameRate, useSubClip)

if __name__ == '__main__':
    main()



# audio = (mpy.AudioFileClip(audioFile))
# clip.audio = audio
# clip.write_videofile(f"./data/output/{now}.mp4", codec="mpeg4", preset="medium") # low quality low size
# clip.write_videofile(f"./data/output/{now}.avi", codec="png", preset="medium") # high quality high size
# clip.write_videofile(f"./data/output/{now}.mp4", preset="slow", threads=3) # high quality low size
