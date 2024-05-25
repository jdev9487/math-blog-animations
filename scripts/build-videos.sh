case $1 in
    l)
        videoDir="480p15"
        ;;
    m)
        videoDir="720p30"
        ;;
    h)
        videoDir="1080p60"
        ;;
    k)
        videoDir="2160p60"
        ;;
esac

mkdir output
for path in animations/**
do
    pythonSource=$path/source.py
    settingSource=$path/settings.yml
    directoryName=$(basename -- "$path")
    manim -q$1 $pythonSource Source
    mv media/videos/source/$videoDir/Source.mp4 output/$directoryName.mp4

    timestamp=$(yq '.thumbnail' "./$settingSource")
    ffmpeg -i output/$directoryName.mp4 -ss $timestamp -vframes 1 output/$directoryName.png
done
rm -rf media