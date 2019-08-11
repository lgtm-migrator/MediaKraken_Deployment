"""
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
"""

DEVICE_ITEM_TYPES = [
    "Amplifier",
    "Blu-ray Player",
    "Blu-ray Ultra HD Player",
    "Cable Box",
    "CD Player",
    "Chromecast",
    "Chromecast Ultra",
    "DAC",
    "DAT",
    "DVD Player",
    "DVR",
    "Game System",
    "HD-DVD Player",
    "HDHomeRun",
    "Internet Radio",
    "LaserDisc",
    "MiniDisc",
    "MUSE Laserdisc",
    "OTA Tuner",
    "PC",
    "Preamplifier",
    "Projector",
    "Radio",
    "Receiver",
    "Roku",
    "SACD",
    "Satellite Receiver",
    "Screen",
    "Tape Deck",
    "Television",
    "Tuner",
    "Turntable",
    "VCR - SVHS",
    "VCR - VHS",
    "VCR - Beta",
    "VCR - Super Beta",
    "Video Processor",
    "Video Switcher",
]

DEVICE_COMMANDS = {
    "Manufacturer": "Base",
    "Item Type": "Base",
    "Model Support":
        {
            "Generic": "Generic Base Name"
        },

    "Protocol":
        {
            "//": "EISCP, IR, Kodi, LAN, RS232, Serial, Telnet",
            "Method:": "RS232",
            "Baud Rate": "9600",
            "Data Length": "8",
            "Parity Bit": "None",
            "Start Bit": None,
            "Stop Bit": "1",
            "Flow Control": "None",
            "Emulation": None,
            "Transmission Method": None,
            "Hardware Port": None,
            "Host IP": None,
            "Host Port": None,
            "User": None,
            "Password": None,
        },

    "Application":
        {
            "Amazon Instant Video": None,
            "HBO Go": None,
            "Hulu Plus": None,
            "Kodi": None,
            "Netflix": None,
            "Pandora": None,
            "Plex": None,
            "SiriusXM": None,
            "sling TV": None,
            "Vudu": None,
        },

    "Aspect Ratio":
        {
            "Next Ratio": None,
            "Auto": None,
            "Native": None,
            "Letterbox": None,
            "Real": None,
            "4:3": None,
            "1:1": None,
            "1:33": None,
            "1:55": None,
            "1:66": None,
            "1:78": None,
            "1.85": None,
            "2.35": None,
            "16:9": None,
            "16:10": None,
        },

    "Character":
        {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
            "H": None,
            "I": None,
            "J": None,
            "K": None,
            "L": None,
            "M": None,
            "N": None,
            "O": None,
            "P": None,
            "Q": None,
            "R": None,
            "S": None,
            "T": None,
            "U": None,
            "V": None,
            "W": None,
            "X": None,
            "Y": None,
            "Z": None,
        },

    "Error Codes":
        {
            "Not Supported": None,
        },

    "Devices":
        {
            "IPOD":
                {
                    "ALBUM NEXT": None,
                    "ALBUM PREVIOUS": None,
                    "BACKLIGHT": None,
                    "BROWSE MODE": None,
                    "CHAPTER NEXT": None,
                    "CHAPTER PREVIOUS": None,
                    "CURSOR DOWN": None,
                    "CURSOR ENTER": None,
                    "CURSOR LEFT": None,
                    "CURSOR RIGHT": None,
                    "CURSOR UP": None,
                    "DISPLAY": None,
                    "DOCK CONNECT": None,
                    "DOCK DISCONNECT": None,
                    "ENTER": None,
                    "FORWARD": None,
                    "MENU": None,
                    "MENU BROWSE": None,
                    "MODE": None,
                    "MUTE TOGGLE": None,
                    "NEXT": None,
                    "OSD TOGGLE PHOTO": None,
                    "PAGE DOWN": None,
                    "PAGE UP": None,
                    "PAIRING": None,
                    "PAIRING CANCEL": None,
                    "PARING": None,
                    "PARING CANCEL": None,
                    "PAUSE": None,
                    "PLAY": None,
                    "PLAY PAUSE": None,
                    "PLAY PAUSE TOGGLE": None,
                    "PLAYLIST NEXT": None,
                    "PLAYLIST PREVIOUS": None,
                    "POWER OFF": None,
                    "POWER ON": None,
                    "POWER TOGGLE": None,
                    "PREVIOUS": None,
                    "RANDOM": None,
                    "REMOTE MODE": None,
                    "REPEAT": None,
                    "REPEAT ALL": None,
                    "REPEAT OFF": None,
                    "REPEAT ONE": None,
                    "RETURN": None,
                    "REVERSE": None,
                    "SEARCH DOWN": None,
                    "SEARCH UP": None,
                    "SELECT": None,
                    "SHUFFLE": None,
                    "SHUFFLE ALBUMS": None,
                    "SHUFFLE OFF": None,
                    "SHUFFLE SONGS": None,
                    "SIMPLE REMOTE": None,
                    "SKIP DOWN": None,
                    "SKIP UP": None,
                    "STOP": None,
                    "TOP MENU": None,
                }
        },

    "Hardware":
        {
            "Channel": None,
            "CRT Blue": None,
            "CRT Green": None,
            "CRT Red": None,
            "Cut-Off": None,
            "Lamp Hour Reset": None,
            "Luminance": None,
            "Optical Zoom Shift": None,
            "Optical Focus Shift": None,
            "Projection Mode": None,
            "Reset": None,
            "Shutter Off": None,
            "Shutter On": None,
            "Unit": None,
            "Whisper Mode": None,
        },

    "Misc":
        {
            "Background": None,
            "Closed Caption Display": None,
            "Film Mode": None,
            "Freeze": None,
            "Freeze Off": None,
            "Freeze On": None,
            "Language": None,
            "OSD": None,
            "OSD Off": None,
            "OSD On": None,
            "Startup Image No": None,
            "Startup Image Yes": None,
        },

    "Navigation":
        {
            "Back": None,
            "Channel":
                {
                    "Channel": None,
                    "Channel 1": None,
                    "Channel 2": None,
                    "Channel 3": None,
                    "Channel 4": None,
                    "Channel 5": None,
                    "Channel 6": None,
                    "Channel 7": None,
                    "Channel 8": None,
                    "Channel 9": None,
                    "Channel 10": None,
                    "Channel 11": None,
                    "Channel 12": None,
                    "Channel 13": None,
                    "Channel 14": None,
                    "Channel 15": None,
                    "Channel 16": None,
                    "Channel 17": None,
                    "Channel 18": None,
                    "Channel 19": None,
                    "Channel 20": None,
                    "Channel 21": None,
                    "Channel 22": None,
                    "Channel 23": None,
                    "Channel 24": None,
                    "Channel 25": None,
                    "Channel 26": None,
                    "Channel 27": None,
                    "Channel 28": None,
                    "Channel 29": None,
                    "Channel 30": None,
                    "Channel 31": None,
                    "Channel 32": None,
                    "Channel 33": None,
                    "Channel 34": None,
                    "Channel 35": None,
                    "Channel 36": None,
                    "Channel 37": None,
                    "Channel 38": None,
                    "Channel 39": None,
                    "Channel 40": None,
                    "Channel 41": None,
                    "Channel 42": None,
                    "Channel 43": None,
                    "Channel 44": None,
                    "Channel 45": None,
                    "Channel 46": None,
                    "Channel 47": None,
                    "Channel 48": None,
                    "Channel 49": None,
                    "Channel 50": None,
                    "Channel 51": None,
                    "Channel 52": None,
                    "Channel 53": None,
                    "Channel 54": None,
                    "Channel 55": None,
                    "Channel 56": None,
                    "Channel 57": None,
                    "Channel 58": None,
                    "Channel 59": None,
                    "Channel 60": None,
                    "Channel 61": None,
                    "Channel 62": None,
                    "Channel 63": None,
                    "Channel 64": None,
                    "Channel 65": None,
                    "Channel 66": None,
                    "Channel 67": None,
                    "Channel 68": None,
                    "Channel 69": None,
                    "Channel 70": None,
                    "Channel 71": None,
                    "Channel 72": None,
                    "Channel 73": None,
                    "Channel 74": None,
                    "Channel 75": None,
                    "Channel 76": None,
                    "Channel 77": None,
                    "Channel 78": None,
                    "Channel 79": None,
                    "Channel 80": None,
                    "Channel 81": None,
                    "Channel 82": None,
                    "Channel 83": None,
                    "Channel 84": None,
                    "Channel 85": None,
                    "Channel 86": None,
                    "Channel 87": None,
                    "Channel 88": None,
                    "Channel 89": None,
                    "Channel 90": None,
                    "Channel 91": None,
                    "Channel 92": None,
                    "Channel 93": None,
                    "Channel 94": None,
                    "Channel 95": None,
                    "Channel 96": None,
                    "Channel 97": None,
                    "Channel 98": None,
                    "Channel 99": None,
                    "Channel 100": None,
                    "Channel 101": None,
                    "Channel 102": None,
                    "Channel 103": None,
                    "Channel 104": None,
                    "Channel 105": None,
                    "Channel 106": None,
                    "Channel 107": None,
                    "Channel 108": None,
                    "Channel 109": None,
                    "Channel 110": None,
                    "Channel 111": None,
                    "Channel 112": None,
                    "Channel 113": None,
                    "Channel 114": None,
                    "Channel 115": None,
                    "Channel 116": None,
                    "Channel 117": None,
                    "Channel 118": None,
                    "Channel 119": None,
                    "Channel 120": None,
                    "Channel 121": None,
                    "Channel 122": None,
                    "Channel 123": None,
                    "Channel 124": None,
                    "Channel 125": None,
                    "Channel 126": None,
                    "Channel 127": None,
                    "Channel 128": None,
                    "Channel 129": None,
                    "Channel 130": None,
                    "Channel 131": None,
                    "Channel 132": None,
                    "Channel 133": None,
                    "Channel 134": None,
                    "Channel 135": None,
                    "Channel 136": None,
                    "Channel 137": None,
                    "Channel 138": None,
                    "Channel 139": None,
                    "Channel 140": None,
                    "Channel 141": None,
                    "Channel 142": None,
                    "Channel 143": None,
                    "Channel 144": None,
                    "Channel 145": None,
                    "Channel 146": None,
                    "Channel 147": None,
                    "Channel 148": None,
                    "Channel 149": None,
                    "Channel 150": None,
                    "Channel 151": None,
                    "Channel 152": None,
                    "Channel 153": None,
                    "Channel 154": None,
                    "Channel 155": None,
                    "Channel 156": None,
                    "Channel 157": None,
                    "Channel 158": None,
                    "Channel 159": None,
                    "Channel 160": None,
                    "Channel 161": None,
                    "Channel 162": None,
                    "Channel 163": None,
                    "Channel 164": None,
                    "Channel 165": None,
                    "Channel 166": None,
                    "Channel 167": None,
                    "Channel 168": None,
                    "Channel 169": None,
                    "Channel 170": None,
                    "Channel 171": None,
                    "Channel 172": None,
                    "Channel 173": None,
                    "Channel 174": None,
                    "Channel 175": None,
                    "Channel 176": None,
                    "Channel 177": None,
                    "Channel 178": None,
                    "Channel 179": None,
                    "Channel 180": None,
                    "Channel 181": None,
                    "Channel 182": None,
                    "Channel 183": None,
                    "Channel 184": None,
                    "Channel 185": None,
                    "Channel 186": None,
                    "Channel 187": None,
                    "Channel 188": None,
                    "Channel 189": None,
                    "Channel 190": None,
                    "Channel 191": None,
                    "Channel 192": None,
                    "Channel 193": None,
                    "Channel 194": None,
                    "Channel 195": None,
                    "Channel 196": None,
                    "Channel 197": None,
                    "Channel 198": None,
                    "Channel 199": None,
                    "Channel 200": None,
                    "Channel 201": None,
                    "Channel 202": None,
                    "Channel 203": None,
                    "Channel 204": None,
                    "Channel 205": None,
                    "Channel 206": None,
                    "Channel 207": None,
                    "Channel 208": None,
                    "Channel 209": None,
                    "Channel 210": None,
                    "Channel 211": None,
                    "Channel 212": None,
                    "Channel 213": None,
                    "Channel 214": None,
                    "Channel 215": None,
                    "Channel 216": None,
                    "Channel 217": None,
                    "Channel 218": None,
                    "Channel 219": None,
                    "Channel 220": None,
                    "Channel 221": None,
                    "Channel 222": None,
                    "Channel 223": None,
                    "Channel 224": None,
                    "Channel 225": None,
                    "Channel 226": None,
                    "Channel 227": None,
                    "Channel 228": None,
                    "Channel 229": None,
                    "Channel 230": None,
                    "Channel 231": None,
                    "Channel 232": None,
                    "Channel 233": None,
                    "Channel 234": None,
                    "Channel 235": None,
                    "Channel 236": None,
                    "Channel 237": None,
                    "Channel 238": None,
                    "Channel 239": None,
                    "Channel 240": None,
                    "Channel 241": None,
                    "Channel 242": None,
                    "Channel 243": None,
                    "Channel 244": None,
                    "Channel 245": None,
                    "Channel 246": None,
                    "Channel 247": None,
                    "Channel 248": None,
                    "Channel 249": None,
                    "Channel 250": None,
                    "Channel 251": None,
                    "Channel 252": None,
                    "Channel 253": None,
                    "Channel 254": None,
                    "Channel 255": None,
                },
            "Chapter Forward": None,
            "Chapter Rewind": None,
            "Down": None,
            "Enter/Ok": None,
            "Escape": None,
            "Exit": None,
            "Fast Forward": None,
            "Fast Rewind": None,
            "Help": None,
            "Home": None,
            "Info": None,
            "Left": None,
            "Menu": None,
            "Pause": None,
            "Play": None,
            "Record": None,
            "Return": None,
            "Right": None,
            "Show Context": None,
            "Step": None,
            "Step Forward": None,
            "Step Rewind": None,
            "Still": None,
            "Stop": None,
            "Test": None,
            "Up": None,
        },

    "Numeric":
        {
            "One": None,
            "Two": None,
            "Three": None,
            "Four": None,
            "Five": None,
            "Six": None,
            "Seven": None,
            "Eight": None,
            "Nine": None,
            "Ten": None,
            "Zero": None,
        },

    "PIP":
        {
            "Active": None,
            "Alternate": None,
            "Audio": None,
            "Down": None,
            "Input": None,
            "Input1": None,
            "Input2": None,
            "Input3": None,
            "Input4": None,
            "Input5": None,
            "Off": None,
            "PIP": None,
            "Quad": None,
            "Select": None,
            "Shift": None,
            "Up": None,
            "Zoom": None,
        },

    "Power":
        {
            "On": None,
            "Off": None,
            "Standby": None,
            "Status": None,
        },

    "Query":
        {
            "Library":
                {
                    "Media":
                        {
                            "Albums": None,
                            "Artists": None,
                            "Movies": None,
                            "Music Videos": None,
                            "Songs": None,
                            "TV Shows": None,
                        },
                    "Playlist":
                        {
                            "Audio": None,
                            "Music Video": None,
                            "Video": None,
                        }
                },
            "API Commands": None,
            "Aspect Ratio": None,
            "Blank Status": None,
            "Brightness": None,
            "Codec (Playing Media)": None,
            "Color (Video)": None,
            "Color Mode": None,
            "Color Temp": None,
            "Company Name": None,
            "Contrast": None,
            "Density": None,
            "Error Status": None,
            "Filter Time": None,
            "Gain Green": None,
            "Gain Blue": None,
            "Gain Red": None,
            "Input Selected": None,
            "Lamp Hours": None,
            "Lamp Off": None,
            "Lamp On": None,
            "Lamp On/Off": None,
            "Model Name": None,
            "Mute Status": None,
            "Native Resolution": None,
            "Overscan Ratio": None,
            "Projection Mode": None,
            "Serial Number": None,
            "Sharpness": None,
            "Status": None,
            "Tint (Video)": None,
            "Volume": None,
        },

    "Sound":
        {
            "Auddysey":
                {
                    "Dynamic EQ": None,
                    "Dynamic EQ Offset": None,
                    "Dynamic EQ Offset -5db": None,
                    "Dynamic EQ Offset -10db": None,
                    "Dynamic EQ Offset -15db": None,
                    "Dynamic EQ Offset Off": None,
                    "Dynamic EQ Vol": None,
                    "Dynamic Off": None,
                    "Dynamic On": None,
                    "Dynamic Volume Mode": None,
                    "Dynamic Volume Mode H": None,
                    "Dynamic Volume Mode L": None,
                    "Dynamic Volume Mode M": None,
                    "Dynamic Volume Mode Off": None,
                    "Dynamic Multi EQ": None,
                    "Dynamic Multi EQ Down": None,
                    "Dynamic Multi EQ Mem 1": None,
                    "Dynamic Multi EQ Mem 3": None,
                    "Dynamic Multi EQ Mem 4": None,
                    "Dynamic Multi EQ Mem 5": None,
                    "Dynamic Multi EQ Off": None,
                    "Dynamic Multi EQ Up": None,
                },
            "Mute On": None,
            "Mute Off": None,
            "Mute Status": None,
            "Surround":
                {
                },
            "Treble":
                {
                },
            "Volume Status": None,
            "Volume Set": None,
            "Volume Down": None,
            "Volume Up": None,
            "Volume Up Zone 1": None,
            "Volume Up Zone 2": None,
            "Volume Up Zone 3": None,
            "Volume Up Zone 4": None,
            "Volume Up Zone 5": None,
            "Volume Up Zone 6": None,
            "Volume Up Zone 7": None,
            "Volume Up Zone 8": None,
            "Volume Down Zone 1": None,
            "Volume Down Zone 2": None,
            "Volume Down Zone 3": None,
            "Volume Down Zone 4": None,
            "Volume Down Zone 5": None,
            "Volume Down Zone 6": None,
            "Volume Down Zone 7": None,
            "Volume Down Zone 8": None,
            "Volume +3db": None,
            "Volume -3db": None,
            "Volume +10": None,
            "Volume -10": None,
            "Volume -15db": None,
            "Volume -20db": None,
            "Volume -30db": None,
            "Volume -40db": None,
            "Volume -50db": None,
            "Volume -60db": None,
            "Volume -70db": None,
            "Volume Recall 1": None,
            "Volume Recall 2": None,
            "Volume Recall 3": None,
            "Volume Recall 4": None,
            "Volume Recall 5": None,
            "Volume Recall 6": None,
            "Volume Recall 7": None,
            "Volume Recall 8": None,
            "Volume Recall 9": None,
            "Volume Recall 10": None,
        },

    "Source":
        {
            "AUX1": None,
            "AUX2": None,
            "AUX3": None,
            "BluRay": None,
            "BluRay UHD": None,
            "Cable/TV": None,
            "Coax1": None,
            "Coax2": None,
            "Coax3": None,
            "Composite": None,
            "Composite1": None,
            "Composite2": None,
            "Composite3": None,
            "CompositeA": None,
            "CompositeC": None,
            "CompositeE": None,
            "CompositeF": None,
            "Component": None,
            "Component1": None,
            "Component2": None,
            "Component3": None,
            "Component4": None,
            "DVD": None,
            "DVD1": None,
            "DVD2": None,
            "DVR": None,
            "Game": None,
            "Game1": None,
            "Game2": None,
            "HDMI": None,
            "HDMI1": None,
            "HDMI2": None,
            "HDMI3": None,
            "HDMI4": None,
            "HDMI5": None,
            "HDMI6": None,
            "HDMI7": None,
            "HDMI8": None,
            "Input": None,
            "Ipod": None,
            "IRadio": None,
            "LaserDisc": None,
            "LaserDisc1": None,
            "LaserDisc2": None,
            "Net/USB": None,
            "Phono": None,
            "RGB1": None,
            "RGB2": None,
            "SACD": None,
            "Satellite": None,
            "S-Video": None,
            "S-Video1": None,
            "S-Video2": None,
            "S-Video3": None,
            "SD Card": None,
            "Tape": None,
            "Tape1": None,
            "Tape2": None,
            "Tuner": None,
            "Tuner1": None,
            "Tuner2": None,
            "Tuner3": None,
            "Turntable": None,
            "USB": None,
            "VCR": None,
            "VCR1": None,
            "VCR2": None,
            "VCR3": None,
            "VCR4": None,
        },

    "Video Calibration":
        {
            "Black Level": None,
            "Brightness": None,
            "Brightness Down": None,
            "Brightness Up": None,
            "Color": None,
            "Color Temperature": None,
            "Color Temp R": None,
            "Color Temp G": None,
            "Color Temp B": None,
            "Color Balance R": None,
            "Color Balance G": None,
            "Color Balance B": None,
            "Color Density Down": None,
            "Color Density Up": None,
            "Contrast": None,
            "Contrast +30": None,
            "Contrast -30": None,
            "Contrast Up": None,
            "Contrast Down": None,
            "Convergance":
                {
                    "Blanking": None,
                    "Blanking Off": None,
                    "Blanking On": None,
                    "Bow": None,
                    "Dynamic": None,
                    "Edge Linearity": None,
                    "Keystone": None,
                    "Keystone Down": None,
                    "Keystone Left": None,
                    "Keystone Right": None,
                    "Keystone Up": None,
                    "Linearity": None,
                    "Phase": None,
                    "Pincushion": None,
                    "Shift": None,
                    "Size": None,
                    "Skew": None,
                    "Static": None,
                    "Quandrant Top Left": None,
                    "Quandrant Top": None,
                    "Quandrant Top Right": None,
                    "Quandrant Right": None,
                    "Quandrant Left": None,
                    "Quandrant Bottom Left": None,
                    "Quandrant Bottom Right": None,
                    "Quandrant Bottom": None,
                    "Veritcal Center": None,
                    "Verticle Keystone Down": None,
                    "Verticle Keystone Up": None,
                    "Verticle Shift Down": None,
                    "Verticle Shift Up": None,
                    "Verticle Shift 0": None,
                    "Verticle Shift 20": None,
                    "Verticle Shift 40": None,
                    "Verticle Shift 60": None,
                    "Verticle Shift 80": None,
                    "Verticle Shift 100": None,
                    "Vertical Size": None,
                },
            "Detail": None,
            "Detail Down": None,
            "Detail Up": None,
            "Gain": None,
            "Gain Down": None,
            "Gain Up": None,
            "Gamma": None,
            "Gamma Down": None,
            "Gamma Up": None,
            "Hue": None,
            "Hue Down": None,
            "Hue Up": None,
            "Overscan Down": None,
            "Overscan Off": None,
            "Overscan On": None,
            "Overscan Up": None,
            "Test":
                {
                    "On": None,
                    "Patterns":
                        {
                            "IRE 10": None,
                            "IRE 20": None,
                            "IRE 30": None,
                            "IRE 40": None,
                            "IRE 50": None,
                            "IRE 60": None,
                            "IRE 70": None,
                            "IRE 80": None,
                            "IRE 90": None,
                            "IRE 100": None,
                        }
                },
            "Tint": None,
            "Tint Down": None,
            "Tint Up": None,
            "Sharpness": None,
            "Sharpness Down": None,
            "Sharpness Up": None,
            "Underscan":
                {
                    "0": None,
                    "10": None,
                    "12.5": None,
                    "15": None,
                    "20": None,
                    "5": None,
                }
        },

    "Zone":
        {
            "A1": None,
            "A2": None,
            "A3": None,
            "A4": None,
            "A5": None,
            "A6": None,
            "B1": None,
            "B2": None,
            "B3": None,
            "B4": None,
            "B5": None,
            "B6": None,
            "C1": None,
            "C2": None,
            "C3": None,
            "C4": None,
            "C5": None,
            "C6": None,
            "D1": None,
            "D2": None,
            "D3": None,
            "D4": None,
            "D5": None,
            "D6": None,
            "Z1": None,
            "Z2": None,
            "Z3": None,
        },

    "Zoom":
        {
            "Zoom": None,
            "Zoom Down": None,
            "Zoom In": None,
            "Zoom Out": None,
            "Zoom Up": None,
            "Zoom 0": None,
            "Zoom 20": None,
            "Zoom 40": None,
            "Zoom 60": None,
            "Zoom 80": None,
            "Zoom 100": None,
        },
}
