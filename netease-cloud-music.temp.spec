%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:		netease-cloud-music
Version:	${VERSION}
Release:	${RELEASE}
Summary:	Netease Cloud Music (unofficial release, package made by Jason Mun)

Group:		Sound and Video
License:	Proprietary
URL:		https://github.com/yomun/netease-cloud-music-rpm

Source:	   ${SOURCE}

AutoReqProv:	no

Provides:	netease-cloud-music = ${VERSION}-${RELEASE}
Provides:	application(netease-cloud-music.desktop)

Requires:	alsa-lib%{?_isa} >= 1.0.16
Requires:	atk%{?_isa} >= 1.12.4
Requires:	glibc%{?_isa} >= 2.14
Requires:	cairo%{?_isa} >= 1.6.0
Requires:	libcue%{?_isa}
Requires:	dbus%{?_isa} >= 1.2.14
Requires:	expat%{?_isa} >= 2.0.1
Requires:	fontconfig%{?_isa} >= 2.11
Requires:	freetype%{?_isa} >= 2.6
Requires:	libgcc%{?_isa}
Requires:	gdk-pixbuf2%{?_isa} >= 2.22.0
Requires:	glib2%{?_isa} >= 2.37.3
Requires:	gtk2%{?_isa} >= 2.24.0
Requires:	nspr%{?_isa}
Requires:	nss%{?_isa}
Requires:	pango%{?_isa}
Requires:	qt5-qtbase%{?_isa}
Requires:	qt5-qtmultimedia%{?_isa}
Requires:	qt5-qtx11extras%{?_isa}
Requires:	sqlite%{?_isa}
Requires:	libstdc++%{?_isa}
Requires:	taglib%{?_isa} >= 1.8
Requires:	libXcursor%{?_isa}
Requires:	libXext%{?_isa}
Requires:	libXfixes%{?_isa}
Requires:	libXi%{?_isa}
Requires:	libXrandr%{?_isa}
Requires:	libXrender%{?_isa}
Requires:	libXScrnSaver%{?_isa}
Requires:	libXtst%{?_isa}
Requires:	zlib%{?_isa} >= 1.2.3
Requires:	gstreamer1-plugins-ugly-free%{?_isa}

%description
Netease Cloud Music (unofficial release, package made by Jason Mun <yomun@yahoo.com>)

%prep
%setup -q

%build
echo $RPM_BUILD

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mv ./* $RPM_BUILD_ROOT/

%post
gtk-update-icon-cache /usr/share/icons/hicolor

%files
%defattr(-,root,root)
/usr/share/icons/hicolor/scalable/apps/netease-cloud-music.svg
/usr/share/applications/netease-cloud-music.desktop
/usr/lib/netease-cloud-music/locales/*.pak
/usr/lib/netease-cloud-music/cef.pak
/usr/lib/netease-cloud-music/cef_100_percent.pak
/usr/lib/netease-cloud-music/natives_blob.bin
/usr/lib/netease-cloud-music/snapshot_blob.bin
/usr/lib/netease-cloud-music/netease-cloud-music
/usr/lib/netease-cloud-music/cef_extensions.pak
/usr/lib/netease-cloud-music/icudtl.dat
/usr/lib/netease-cloud-music/libcef.so
/usr/lib/netease-cloud-music/chrome-sandbox
/usr/lib/netease-cloud-music/cef_200_percent.pak
# /usr/lib/netease-cloud-music/libcrypto.so.1.0.2
/usr/bin/netease-cloud-music

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Nov 8 2017 Senorsen <yomun@yahoo.com> - 1.0.0-1
- First rpm package! :-)
