#!/bin/bash
mkdir ~/ffmpeg_sources

cd ~/ffmpeg_sources
git clone git://github.com/yasm/yasm.git
cd yasm
./autogen.sh
./configure
make -j8
make install

cd ~/ffmpeg_sources
git clone --depth 1 git://git.videolan.org/x264
cd x264
./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin" --enable-static --disable-opencl
make -j8
make install
make distclean

cd ~/ffmpeg_sources
curl -L -O https://get.videolan.org/x265/x265_2.1.tar.gz
tar xzvf x265_2.1.tar.gz
cd ~/ffmpeg_sources/x265_2.1/build/linux
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="$HOME/ffmpeg_build" -DENABLE_SHARED:bool=off ../../source
make -j8
make install

cd ~/ffmpeg_sources
wget -O fdk-aac.tar.gz https://github.com/mstorsjo/fdk-aac/tarball/master
tar xzvf fdk-aac.tar.gz
cd mstorsjo-fdk-aac*
autoreconf -fiv
./configure --prefix="$HOME/ffmpeg_build" --disable-shared
make -j8
make install
make distclean

cd ~/ffmpeg_sources
curl -L -O http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz
tar xzvf lame-3.99.5.tar.gz
cd lame-3.99.5
./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin" --disable-shared --enable-nasm
make -j8
make install
make distclean

cd ~/ffmpeg_sources
git clone http://git.opus-codec.org/opus.git
cd opus
autoreconf -fiv
./configure --prefix="$HOME/ffmpeg_build" --disable-shared
make -j8
make install
make distclean

cd ~/ffmpeg_sources
curl -O http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz
tar xzvf libogg-1.3.2.tar.gz
cd libogg-1.3.2
./configure --prefix="$HOME/ffmpeg_build" --disable-shared
make -j8
make install
make distclean

cd ~/ffmpeg_sources
curl -O http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.5.tar.gz
tar xzvf libvorbis-1.3.5.tar.gz
cd libvorbis-1.3.5
LDFLAGS="-L$HOME/ffmeg_build/lib" CPPFLAGS="-I$HOME/ffmpeg_build/include" ./configure --prefix="$HOME/ffmpeg_build" --with-ogg="$HOME/ffmpeg_build" --disable-shared
make -j8
make install
make distclean

cd ~/ffmpeg_sources
git clone --depth 1 https://chromium.googlesource.com/webm/libvpx.git
cd libvpx
./configure --prefix="$HOME/ffmpeg_build" --disable-examples --disable-unit-tests
make -j8
make install
make clean

cd ~/ffmpeg_sources
curl -O http://downloads.xiph.org/releases/speex/speexdsp-1.2rc3.tar.gz
tar xzvf speexdsp-1.2rc3.tar.gz
cd speexdsp-1.2rc3
./configure
make -j8
make install

cd ~/ffmpeg_sources
curl -O http://downloads.xvid.org/downloads/xvidcore-1.3.4.tar.gz
tar xzvf xvidcore-1.3.4.tar.gz
cd xvidcore/build/generic
./configure
make -j8
make install

cd ~/ffmpeg_sources
git clone --depth 1 git://source.ffmpeg.org/ffmpeg
cd ffmpeg
PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" ./configure \
    --prefix="$HOME/ffmpeg_build" \
    --pkg-config-flags="--static" \
    --extra-cflags="-I$HOME/ffmpeg_build/include" \
    --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
    --bindir="$HOME/bin" \
    --enable-gpl \
    --enable-nonfree \
    --enable-libass \
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libmp3lame \
    --enable-libopus \
    --enable-libsmbclient \
    --enable-libspeex \
    --enable-libtheora \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxvid \
    --enable-version3
make -j8
make install
make distclean
hash -r
