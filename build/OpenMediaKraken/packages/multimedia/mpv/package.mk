#
#  Copyright (C) 2017 Quinn D Granfor <spootdev@gmail.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  version 2, as published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License version 2 for more details.
#
#  You should have received a copy of the GNU General Public License
#  version 2 along with this program; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

PKG_NAME="mpv"
PKG_VERSION="0.26.0"
PKG_ARCH="any"
PKG_LICENSE="GPL"
PKG_SITE="https://mpv.io/"
PKG_URL="https://github.com/mpv-player/mpv/archive/v$PKG_VERSION.tar.bz2"
PKG_DEPENDS_TARGET="toolchain fontconfig freetype libxml2"
PKG_SECTION="multimedia"
PKG_SHORTDESC="MPV: a free, open source, and cross-platform media player"
PKG_LONGDESC="mpv a free, open source, and cross-platform media player."

PKG_IS_ADDON="no"
PKG_AUTORECONF="no"

