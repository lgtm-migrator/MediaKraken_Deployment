'''
  Copyright (C) 2017 Quinn D Granfor <spootdev@gmail.com>

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

import base64
import socket


class CommonHardwareSamsung(object):
    """
    Class for interfacing with samsung TV equipment over network connection
    """

    def __init__(self, device_ip):
        self.src = '192.168.1.2'  # ip of remote
        self.mac = '00-AB-11-11-11-11'  # mac of remote
        self.remote = 'python remote'  # remote name
        self.dst = device_ip  # ip of tv
        self.app = 'python'  # iphone..iapp.samsung
        self.tv = 'LE32C650'  # iphone.LE32C650.iapp.samsung

    def com_hardware_command(self, key):
        new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new.connect((self.dst, 55000))
        msg = chr(0x64) + chr(0x00) + \
              chr(len(base64.b64encode(self.src))) + chr(0x00) + base64.b64encode(self.src) + \
              chr(len(base64.b64encode(self.mac))) + chr(0x00) + base64.b64encode(self.mac) + \
              chr(len(base64.b64encode(self.remote))) + \
              chr(0x00) + base64.b64encode(self.remote)
        pkt = chr(0x00) + chr(len(self.app)) + chr(0x00) + self.app + \
              chr(len(msg)) + chr(0x00) + msg
        new.send(pkt)
        msg = chr(0x00) + chr(0x00) + chr(0x00) + \
              chr(len(base64.b64encode(key))) + chr(0x00) + base64.b64encode(key)
        pkt = chr(0x00) + chr(len(self.tv)) + chr(0x00) + self.tv + \
              chr(len(msg)) + chr(0x00) + msg
        new.send(pkt)
        new.close()

    def com_hardware_close(self):
        pass


"""
Keycodes

KEY_0
KEY_1
KEY_2
KEY_3
KEY_4
KEY_5
KEY_6
KEY_7
KEY_8
KEY_9
KEY_11
KEY_12
KEY_3SPEED
KEY_4_3
KEY_16_9
KEY_AD
KEY_ADDDEL
KEY_ALT_MHP
KEY_ANGLE
KEY_ANTENA
KEY_ANYNET
KEY_ANYVIEW
KEY_APP_LIST
KEY_ASPECT
KEY_AUTO_ARC_ANTENNA_AIR
KEY_AUTO_ARC_ANTENNA_CABLE
KEY_AUTO_ARC_ANTENNA_SATELLITE
KEY_AUTO_ARC_ANYNET_AUTO_START
KEY_AUTO_ARC_ANYNET_MODE_OK
KEY_AUTO_ARC_AUTOCOLOR_FAIL
KEY_AUTO_ARC_AUTOCOLOR_SUCCESS
KEY_AUTO_ARC_CAPTION_ENG
KEY_AUTO_ARC_CAPTION_KOR
KEY_AUTO_ARC_CAPTION_OFF
KEY_AUTO_ARC_CAPTION_ON
KEY_AUTO_ARC_C_FORCE_AGING
KEY_AUTO_ARC_JACK_IDENT
KEY_AUTO_ARC_LNA_OFF
KEY_AUTO_ARC_LNA_ON
KEY_AUTO_ARC_PIP_CH_CHANGE
KEY_AUTO_ARC_PIP_DOUBLE
KEY_AUTO_ARC_PIP_LARGE
KEY_AUTO_ARC_PIP_LEFT_BOTTOM
KEY_AUTO_ARC_PIP_LEFT_TOP
KEY_AUTO_ARC_PIP_RIGHT_BOTTOM
KEY_AUTO_ARC_PIP_RIGHT_TOP
KEY_AUTO_ARC_PIP_SMALL
KEY_AUTO_ARC_PIP_SOURCE_CHANGE
KEY_AUTO_ARC_PIP_WIDE
KEY_AUTO_ARC_RESET
KEY_AUTO_ARC_USBJACK_INSPECT
KEY_AUTO_FORMAT
KEY_AUTO_PROGRAM
KEY_AV1
KEY_AV2
KEY_AV3
KEY_BACK_MHP
KEY_BOOKMARK
KEY_CALLER_ID
KEY_CAPTION
KEY_CATV_MODE
KEY_CHDOWN
KEY_CHUP
KEY_CH_LIST
KEY_CLEAR
KEY_CLOCK_DISPLAY
KEY_COMPONENT1
KEY_COMPONENT2
KEY_CONTENTS
KEY_CONVERGENCE
KEY_CONVERT_AUDIO_MAINSUB
KEY_CUSTOM
KEY_CYAN
KEY_DEVICE_CONNECT
KEY_DISC_MENU
KEY_DMA
KEY_DNET
KEY_DNIe
KEY_DNSe
KEY_DOOR
KEY_DOWN
KEY_DSS_MODE
KEY_DTV
KEY_DTV_LINK
KEY_DTV_SIGNAL
KEY_DVD_MODE
KEY_DVI
KEY_DVR
KEY_DVR_MENU
KEY_DYNAMIC
KEY_ENTER
KEY_ENTERTAINMENT
KEY_ESAVING
KEY_EXIT
KEY_EXT1
KEY_EXT2
KEY_EXT3
KEY_EXT4
KEY_EXT5
KEY_EXT6
KEY_EXT7
KEY_EXT8
KEY_EXT9
KEY_EXT10
KEY_EXT11
KEY_EXT12
KEY_EXT13
KEY_EXT14
KEY_EXT15
KEY_EXT16
KEY_EXT17
KEY_EXT18
KEY_EXT19
KEY_EXT20
KEY_EXT21
KEY_EXT22
KEY_EXT23
KEY_EXT24
KEY_EXT25
KEY_EXT26
KEY_EXT27
KEY_EXT28
KEY_EXT29
KEY_EXT30
KEY_EXT31
KEY_EXT32
KEY_EXT33
KEY_EXT34
KEY_EXT35
KEY_EXT36
KEY_EXT37
KEY_EXT38
KEY_EXT39
KEY_EXT40
KEY_EXT41
KEY_FACTORY
KEY_FAVCH
KEY_FF
KEY_FF_
KEY_FM_RADIO
KEY_GAME
KEY_GREEN
KEY_GUIDE
KEY_HDMI
KEY_HDMI1
KEY_HDMI2
KEY_HDMI3
KEY_HDMI4
KEY_HELP
KEY_HOME
KEY_ID_INPUT
KEY_ID_SETUP
KEY_INFO
KEY_INSTANT_REPLAY
KEY_LEFT
KEY_LINK
KEY_LIVE
KEY_MAGIC_BRIGHT
KEY_MAGIC_CHANNEL
KEY_MDC
KEY_MENU
KEY_MIC
KEY_MORE
KEY_MOVIE1
KEY_MS
KEY_MTS
KEY_MUTE
KEY_NINE_SEPERATE
KEY_OPEN
KEY_PANNEL_CHDOWN
KEY_PANNEL_CHUP
KEY_PANNEL_ENTER
KEY_PANNEL_MENU
KEY_PANNEL_POWER
KEY_PANNEL_SOURCE
KEY_PANNEL_VOLDOW
KEY_PANNEL_VOLUP
KEY_PANORAMA
KEY_PAUSE
KEY_PCMODE
KEY_PERPECT_FOCUS
KEY_PICTURE_SIZE
KEY_PIP_CHDOWN
KEY_PIP_CHUP
KEY_PIP_ONOFF
KEY_PIP_SCAN
KEY_PIP_SIZE
KEY_PIP_SWAP
KEY_PLAY
KEY_PLUS100
KEY_PMODE
KEY_POWER
KEY_POWEROFF
KEY_POWERON
KEY_PRECH
KEY_PRINT
KEY_PROGRAM
KEY_QUICK_REPLAY
KEY_REC
KEY_RED
KEY_REPEAT
KEY_RESERVED1
KEY_RETURN
KEY_REWIND
KEY_REWIND_
KEY_RIGHT
KEY_RSS
KEY_RSURF
KEY_SCALE
KEY_SEFFECT
KEY_SETUP_CLOCK_TIMER
KEY_SLEEP
KEY_SOUND_MODE
KEY_SOURCE
KEY_SRS
KEY_STANDARD
KEY_STB_MODE
KEY_STILL_PICTURE
KEY_STOP
KEY_SUB_TITLE
KEY_SVIDEO1
KEY_SVIDEO2
KEY_SVIDEO3
KEY_TOOLS
KEY_TOPMENU
KEY_TTX_MIX
KEY_TTX_SUBFACE
KEY_TURBO
KEY_TV
KEY_TV_MODE
KEY_UP
KEY_VCHIP
KEY_VCR_MODE
KEY_VOLDOWN
KEY_VOLUP
KEY_WHEEL_LEFT
KEY_WHEEL_RIGHT
KEY_W_LINK
KEY_YELLOW
KEY_ZOOM1
KEY_ZOOM2
KEY_ZOOM_IN
KEY_ZOOM_MOVE
KEY_ZOOM_OUT
"""
