mkdir output
for path in animations/**
do
    pythonSource=$path/source.py
    settingSource=$path/settings.yml
    timestamp=(yq '.thumbnail' $settingSource)
    directoryName=$(basename -- "$path")
    updatedSource="$path/$directoryName.py"
    mv "./$pythonSource" "./$updatedSource"
    manim -qk $updatedSource Source
    mv media/videos/$directoryName/2160p60/*.mp4 output/$directoryName.mp4

    timestamp=$(yq '.thumbnail' "./$settingSource")
    ffmpeg -i output/$directoryName.mp4 -ss $timestamp -vframes 1 output/$directoryName.png
done
rm -rf media