xvfb-run manimgl ind.py -w -r 2160x3840 --fps 60
# ffmpeg -i my.mov -c copy -movflags +faststart -bsf:a aac_adtstoasc patched_video.mov
./g