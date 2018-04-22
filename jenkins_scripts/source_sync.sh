# broadcast
cp /home/metaman/MediaKraken_Deployment/source/subprogram_broadcast.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenBroadcast/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenBroadcast/src/.

# debug
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenDebug/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_debug.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenDebug/src/.

# devicescanner
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenDevicescan/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_hardware_discover.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenDevicescan/src/.

# download
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenDownload/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_download.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenDownload/src/.

# metadata
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/database /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/metadata /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_server_metadata_api.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_server_metadata_api_worker.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp /home/metaman/MediaKraken_Deployment/source/build_image_directory.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp /home/metaman/MediaKraken_Deployment/source/build_trailer_directory.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp /home/metaman/MediaKraken_Deployment/source/subprogram*.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.
cp /home/metaman/MediaKraken_Deployment/source/bulk_themoviedb_netfetch.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenMetadata/src/.

# ripper
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenRipper/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_ripper.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenRipper/src/.

# server
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/database /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/network /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.
cp /home/metaman/MediaKraken_Deployment/source/db_create_update.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.
cp /home/metaman/MediaKraken_Deployment/source/db_update_version.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_server.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_server_link.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.
cp /home/metaman/MediaKraken_Deployment/source/subprogram*.py  /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenServer/src/.

# slave
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenSlave/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/common/common_docker.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenSlave/src/stream2chromecast/common/.
cp -R /home/metaman/MediaKraken_Deployment/source/database /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenSlave/src/.
cp /home/metaman/MediaKraken_Deployment/source/main_server_slave.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenSlave/src/.
cp /home/metaman/MediaKraken_Deployment/source/subprogram_ffprobe_metadata.py /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenSlave/src/.

# webserver
cp -R /home/metaman/MediaKraken_Deployment/source/common /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenWebServer/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/database /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenWebServer/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/network /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenWebServer/src/.
cp -R /home/metaman/MediaKraken_Deployment/source/web_app /home/metaman/MediaKraken_Deployment/docker/alpine/ComposeMediaKrakenWebServer/src/.