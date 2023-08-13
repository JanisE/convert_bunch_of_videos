# Compressing a bunch of video files for storage

## Use case

My dashcam is saving video into MOV files taking up about 100 MB per 1 minute.

I want to compress them to take up less space for storage.

Getting ffmpeg to encode the videos to MKV using Nvidia HVEC hardware encoder (CUDA/NVENC) was too difficult for me. On the other hand, Avidemux GUI allows to select Nvidia HVEC encoder and set its options out of the box. So, how to get Avidemux to easily convert a lot of files in one go?

## Converting videos

In Avidemux, if you set all the encoding configuration, you can save it as a Python script (File -> Project Script -> Save As Project). You can then run Avidemux and load the project in one go by
```bash
# (Assuming mov_to_mkv.py is in the current directory.)
/home/path/to/avidemux_2.8.1.appImage --run mov_to_mkv.py
```

I've modified the Python script to actually convert/save the video to a file and apply the conversion for all MOV files within a folder.

This (sample) script contains configuration for converting MOV files to MKV with HVEC video codec using bitrate=3000: [mov_to_mkv.py](mov_to_mkv.py). It produced 3-4 times smaller MKV video files than the original MOVs.

In addition, I use script [adjust_timestamps.sh](adjust_timestamps.sh) in order to set file timestamps to the new files from the original ones. This may be useful if the original files do have the actual correct timestamps of the recording.
```bash
# Place the file and execute this in the folder containing the original MOVs and the new MKVs:
./adjust_timestamps.sh
```

## Room for Improvement

### Directory of files to be converted

The Avidemux Python scripts support a small subset of the actual Python (more documentation available in an [Avidemux forum thread](https://avidemux.org/smif/index.php?topic=19390.0), so I did not manage to pass in the **directory** dynamically – it is to be edited in the script code.

### GUI popping up

Executing the Python scripts still calls up Avidemux' GUI window, and focuses it upon converting each next video. You can probably do the conversion using Avidemux's CLI only, but then you cannot use the easy option to set up the configuration in GUI and use it in the script.