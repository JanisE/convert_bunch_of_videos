#PY  <- Needed to identify #

# Converts all MOV files (from Navitel R300 GPS) to 3-4 times smaller (bitrate=3000) MKVs using NVidia's HEVC encoder.

# TODO Is it possible to get the current working directory here? Or by some parameter?
directory = "/vol/Ciba/Foto/2023/2023-08-05/Auto/tmp"

adm = Avidemux()

for filepath in get_folder_content(directory, "MOV"):
    if not adm.loadVideo(filepath):
        raise(filepath)
    adm.clearSegments()
    adm.addSegment(0, 0, 120253000)
    adm.markerA = 0
    adm.markerB = 120253000
    adm.setPostProc(3, 3, 0)
    adm.setHDRConfig(1, 1, 1, 1, 0)
    adm.videoCodec("ffNvEncHEVC", "preset=5", "profile=0", "rc_mode=0", "quality=20", "bitrate=3000", "max_bitrate=10000", "gopsize=100", "refs=0", "bframes=0", "b_ref_mode=2", "lookahead=0", "aq_strength=1", "spatial_aq=False", "temporal_aq=False"
    , "weighted_pred=False")
    adm.audioClearTracks()
    adm.setSourceTrackLanguage(0,"eng")
    if adm.audioTotalTracksCount() <= 0:
        raise("Cannot add audio track 0, total tracks: " + str(adm.audioTotalTracksCount()))
    adm.audioAddTrack(0)
    adm.audioCodec(0, "LavAAC", "bitrate=128")
    adm.audioSetDrc2(0, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(0, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(0, 0, 0)
    adm.setContainer("MKV", "forceAspectRatio=False", "displayWidth=1280", "displayAspectRatio=2", "addColourInfo=False", "colMatrixCoeff=2", "colRange=0", "colTransfer=2", "colPrimaries=2")

    adm.save(filepath + '_hevc_3000.mkv');
