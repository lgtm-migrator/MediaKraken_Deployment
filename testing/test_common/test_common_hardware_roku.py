'''
  Copyright (C) 2016 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''


from __future__ import absolute_import, division, print_function, unicode_literals
import pytest
import sys
sys.path.append("../common")
from MK_Common_Hardware_Roku import *


@pytest.mark.parametrize(("filename"), [
    ("./cache/BigBuckBunny.ogv"),
    ("./cache/BigBuckBunny_512kb.mp4"),
    ("./cache/fake_video.mp4")])
def test_getMP4Info(filename):
    getMP4Info(filename)


# def extractImages(videoFile, directory, interval, mode=0, offset=0):


# def makeBIF(filename, directory, interval):


# def MK_Common_Roku_Create_BIF(videoFile, first_image_offset=7, image_interval=10, option_mode=0):
