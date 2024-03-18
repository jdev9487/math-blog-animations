mkdir output
for path in *.py
do
    fullfilename=$(basename -- "$path")
    filename="${fullfilename%.*}"
    manim -qh $path Source
    mv media/videos/$filename/1080p60/*.mp4 output/$filename.mp4
done
rm -rf media