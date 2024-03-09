for dir in ./
do
    dir=${dir%*/}
    echo "${dir##*/}"
end