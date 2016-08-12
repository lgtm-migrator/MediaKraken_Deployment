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
from common_system_Sound import *


# text to speech
@pytest.mark.parametrize(("message_to_speak"), [
    ("first test"),
    ("can you hear me again")])
def Test_MK_Sound_Text_To_Speech(message_to_speak):
    MK_Sound_Text_To_Speech(message_to_speak)


# play audio file
@pytest.mark.parametrize(("file_name"), [
    ("./cache/250Hz_44100Hz_16bit_05sec.wav"),
    ("./cache/250Hz_44100Hz_16bit_05sec.mp3")])
def Test_MK_Sound_Play_File(file_name):
    MK_Sound_Play_File(file_name)


# list devices via pyaudio
def Test_com_Audio_Pyaudio_List_Devices():
    com_Audio_Pyaudio_List_Devices()
