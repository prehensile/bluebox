# Installs bluebox on a fresh raspbx install

apt update
apt install python3-pip

pip3 install -r requirements.txt


# TODO: can rsync do this in a less stupid way?
mkdir -p /usr/local/share/bluebox/jukebox/media
mkdir -p /var/lib/asterisk

cp root/etc/asterisk/* /etc/asterisk/
cp root/usr/local/share/bluebox/jukebox/media/* /usr/local/share/bluebox/jukebox/media
cp root/var/lib/asterisk/* /var/lib/asterisk