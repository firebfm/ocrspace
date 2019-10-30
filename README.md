# `ocrspace`

> A Python wrapper for using the [ocr.space API](https://ocr.space/ocrapi).

## Installation
Simply install from `pip`:
```sh
pip install ocrspace
```

## Use
First you'll need to import and instantiate the API wrapper:
```py
import ocrspace
api = ocrspace.API()
# Or if you have an API key or desired language, pass those:
api = ocrspace.API('Insert key here', ocrspace.Language.Croatian)
```
To perform recognition on an image hosted at some URL:
```py
api.ocr_url('URL of image goes here')
```
Or, if you have an image locally upon which to perform recognition:
```py
api.ocr_file('image.jpg')
# or:
api.ocr_file(open('image.jpg', 'rb'))  # or any other file pointer
```
That's it! Look at [`example.py`](example.py) for a demonstration.


## Authorship
This package was created by [Ali Najafi](https://github.com/a4fr) and is maintained by [Erik Boesen](https://github.com/ErikBoesen).

## License
[MIT](LICENSE)

## Added code on how I use it. Check in ocrspace2 folder
Obtain images of subtitles and empty sub.srt timings with VideoSubFinder.

Make a file.txt with all the .jpg filenames
Put everything in one folder and start with command python ocrspace2.py

After you have the extracted subtitle.txt, combine it with empty sub.srt with command python combine.py
