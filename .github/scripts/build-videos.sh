mkdir output
for path in *.py
do
    fullfilename=$(basename -- "$path")
    filename="${fullfilename%.*}"
    manim -iqh $path Source
    mv media/videos/$filename/1080p60/*.gif output/$filename.gif
done
rm -rf media