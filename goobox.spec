%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	CD player and ripper for GNOME
Name:	goobox
Version:	3.6.0
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://www.gnome.org
Source0:	https://download.gnome.org/sources/goobox/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool >= 0.35.0
BuildRequires:	itstool 
BuildRequires:	libxml2-utils
BuildRequires:meson
BuildRequires:ninja
BuildRequires:	pkgconfig(glib-2.0) >= 2.40
BuildRequires:	pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libbrasero-media3)
# Not provided yet
#BuildRequires:	pkgconfig(libcoverart)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libmusicbrainz5) >= 5.0.0
BuildRequires:	pkgconfig(libnotify) >= 0.4.3
BuildRequires:	pkgconfig(sm)
Requires:	gstreamer1.0-plugins-good

%description
Goobox is a CD player and ripper that always knows just what to do.

%files -f %{name}.lang
%doc README NEWS AUTHORS COPYING
%{_bindir}/%{name}
#{_datadir}/GConf/gsettings/%%{name}.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/org.gnome.Goobox.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/metainfo/org.gnome.Goobox.appdata.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%meson -Ddisable-libcoverart=true

%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


