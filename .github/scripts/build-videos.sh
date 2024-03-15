mkdir output
for path in *.py
do
    fullfilename=$(basename -- "$path")
    filename="${fullfilename%.*}"
    manim -qh $path Source
    mv media/videos/$filename/480p15/*.gif output/$filename.gif
done
rm -rf media