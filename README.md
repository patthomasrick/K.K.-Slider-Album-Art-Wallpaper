# K.K. Album Art Wallpaper Generation

Generate a grid of K.K. Slider album arts for usage as a desktop wallpaper!

![Desktop, 1080p](https://github.com/patthomasrick/K.K.-Slider-Album-Art-Wallpaper/releases/download/1.0/kk-desktop-1080p.png)

See [releases](https://github.com/patthomasrick/K.K.-Slider-Album-Art-Wallpaper/releases) for 1080p, 4k versions for desktop and mobile.

## Running the Code

### Prerequisites

First checkout the repository:

```sh
git clone https://github.com/patthomasrick/K.K.-Slider-Album-Art-Wallpaper.git
```

You need Python 3 and ImageMagick. You will also need to install the Python dependencies, namely BeautifulSoup4 and Requests.

```sh
pip install -r requirements.txt
```

To download all of the individual album cover arts, run `kk.py`:

```sh
python kk.py
```

You should see the album cover arts populate the `output` directory.

Now, to generate the wallpapers, run the ImageMagick scripts:

```sh
# Windows
./magick.bat

# Linux
./magick.sh
```

This will create `kk-desktop.png`, `kk-mobile.png` and the respective down-scaled wallpapers that are more suitable for actual use.

## Modifying the Code

### Changing the grid layout

If you are interested in changing the number of columns/rows in the output image, you only need to modify `magick.sh` (or `magick.bat` if you are on Windows):

```sh
magick montage -background transparent -tile 15x -geometry 512x512+40+40 ./output/*.png ./kk-custom.png
```

- Change `15` in `15x` to the number of images per row (essentially the number of columns in the image) you desire.

```sh
magick convert -resize 3840x2160 -background transparent -gravity center -extent 3840x2160 ./kk-custom.png ./kk-custom-downscaled.png
```

- Change `3840x2160` to your desired output resolution. Keep in mind that this command also pads the image with a transparent background so that the output image is exactly that resolution.

## Legal

I do not own or claim to own the rights to the images used. Nintendo Co, Ltd. reserves the rights to the images. I will remove any images and derivative works upon request.

Images are gathered from [Nookpedia](https://nookipedia.com/wiki/List_of_K.K._Slider_songs).
