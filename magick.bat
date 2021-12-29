magick.exe montage -background transparent -tile 15x -geometry 512x512+40+40 ./output/*.png ./kk-desktop.png
magick.exe convert -resize 3840x2160 -background transparent -gravity center -extent 3840x2160 ./kk-desktop.png ./kk-desktop-4k.png
magick.exe convert -resize 1920x1080 -background transparent -gravity center -extent 1920x1080 ./kk-desktop.png ./kk-desktop-1080p.png

magick.exe montage -background transparent -tile 8x -geometry 512x512+40+40 ./output/*.png ./kk-mobile.png
magick.exe convert -resize 2160x3840 -background transparent -gravity center -extent 2160x3840 ./kk-mobile.png ./kk-mobile-4k.png
magick.exe convert -resize 1080x1920 -background transparent -gravity center -extent 1080x1920 ./kk-mobile.png ./kk-mobile-1080p.png
