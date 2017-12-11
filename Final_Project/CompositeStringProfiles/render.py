#!/usr/bin/env python
#Credits to Benjamin Himberg for this script!
"""render.py

Description:
  Uses FFMPEG to create a video from bitmap files in the OUTPUT directory

Usage:
    render.py [options] --input=<val> --scale=<val> --output=<val>

    render.py -h | --help

Options:
  --input=<val>                 Prefix for all bitmap files
  --output=<val>                Prefix for output video
  --scale=<val>                 Resolution of resulting video: eg 500x500
  --sim                         Print resulting command to screen
"""

import os

def main():
    # gather (required) args
    call = 'ffmpeg -framerate 25 -i ./OUTPUT/image_'
    call += '\%06d.png -c:v libx264 -vf fps=25'
    call += ' -pix_fmt yuv420p output.mp4'
    os.system(call)

# ----------------------------------------------------------------------
if __name__ == "__main__": 
    main()
