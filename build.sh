#!/usr/bash/env bash
#
# Author: Jason Mun <yomun@yahoo.com>
# https://github.com/yomun/netease-cloud-music-rpm
#

set -e
set -x

DEBFILENAME="netease-cloud-music_1.1.0_amd64_ubuntu.deb"
# DEBFILENAME="netease-cloud-music_1.0.0-2_amd64_ubuntu16.04.deb"
# DEBFILENAME="netease-cloud-music_1.0.0-2_i386_ubuntu16.04.deb"
# DEBURL="http://s1.music.126.net/download/pc/${DEBFILENAME}"
DEBURL="http://d1.music.126.net/dmusic/${DEBFILENAME}"
VERSION="1.1.0"
RELEASE="0"
ARCH="x86_64" # i686
NAME="netease-cloud-music"
SEMIDIR="$NAME-$VERSION"
FULLDIR="$SEMIDIR-$RELEASE.$ARCH"

cd $(dirname $0)

rm -rf tmp-${ARCH}
mkdir -p tmp-${ARCH}
cd tmp-${ARCH}

mkdir -p dist

SPEC="netease-cloud-music.spec"

cp -rv ../netease-cloud-music.temp.spec "${SPEC}"
sed -i "s/\${VERSION}/${VERSION}/g" "${SPEC}"
sed -i "s/\${RELEASE}/${RELEASE}/g" "${SPEC}"
sed -i "s/\${ARCH}/${ARCH}/g" "${SPEC}"
sed -i "s/\${SOURCE}/${SEMIDIR}.tar.gz/g" "${SPEC}"

rm -rf "${DEBFILENAME}"
wget "${DEBURL}"
ar xf "${DEBFILENAME}"
tar xvf "data.tar.xz"

mkdir -p "${SEMIDIR}"
cp -r usr "${SEMIDIR}/"

mkdir -p "${SEMIDIR}/usr/bin"
rm -rf "${SEMIDIR}/usr/bin/netease-cloud-music"
install -m 755 "../netease-cloud-music" "${SEMIDIR}/usr/bin/netease-cloud-music"

rm -rf "${SEMIDIR}/usr/share/doc/netease-cloud-music/README.md"
rm -rf "${SEMIDIR}/usr/share/doc/netease-cloud-music/changelog.gz"
rm -rf "${SEMIDIR}/usr/share/doc/netease-cloud-music/copyright"

# wget https://dl-http.senorsen.com/2016/05/lib/libcrypto.so.1.0.0-${ARCH} -O ${SEMIDIR}/usr/lib/netease-cloud-music/libcrypto.so.1.0.2

mkdir -p "${HOME}/rpmbuild/SOURCES"
mkdir -p "${HOME}/rpmbuild/SPECS"

tar zcvf "${SEMIDIR}.tar.gz" "${SEMIDIR}"
cp "${SEMIDIR}.tar.gz" "${HOME}/rpmbuild/SOURCES"
cp "${SPEC}" "${HOME}/rpmbuild/SPECS/"

fakeroot rpmbuild -ba "${SPEC}" --target "${ARCH}"

cp "${HOME}/rpmbuild/RPMS/$ARCH/${FULLDIR}.rpm" "${HOME}"

# Clear
rm -rf "../tmp-${ARCH}"

rm -rf "${HOME}/rpmbuild/BUILD/${SEMIDIR}"
rm -rf "${HOME}/rpmbuild/RPMS/${ARCH}"
rm -rf "${HOME}/rpmbuild/SOURCES/${SEMIDIR}.tar.gz"
rm -rf "${HOME}/rpmbuild/SPECS/${SPEC}"
rm -rf "${HOME}/rpmbuild/SRPMS/${SEMIDIR}-${RELEASE}.src.rpm"
