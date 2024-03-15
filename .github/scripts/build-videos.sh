export CLOUDCONVERT_API_KEY=$1
mkdir output
for path in *.py
do
    fullfilename=$(basename -- "$path")
    filename="${fullfilename%.*}"
    manim -qh $path Source
    mv media/videos/$filename/1080p60/*.mp4 output/$filename.mp4
done
rm -rf media

node_modules/cloudconvert-cli/lib/cli.js convert -f gif --outputdir=output/ output/*.mp4