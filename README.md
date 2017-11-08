# netease-cloud-music-rpm
to make & generate netease-cloud-music RPM version<br><br>
First, you need install..<br>
Fedora: $ sudo dnf install rpm-build rpmrebuild rpmlint fakeroot<br><br>
$ cd netease-cloud-music-rpm<br>
$ bash build.sh<br><br>
$ cd ~<br>
$ su<br>
$ rpm -i netease-cloud-music-1.0.0-1.x86_64.rpm<br><br>
$ rpm -qa | grep netease<br>
$ rpm -e netease-cloud-music
