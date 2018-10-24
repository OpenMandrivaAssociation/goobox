%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	CD player and ripper for GNOME
Name:		goobox
Version:	3.4.3
Release:	1
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Sound
Url:		http://www.gnome.org
BuildRequires:	pkgconfig(glib-2.0) >= 2.28
BuildRequires:	pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libbrasero-media3)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libmusicbrainz5) >= 5.0.0
BuildRequires:	pkgconfig(libnotify) >= 0.4.3
BuildRequires:	pkgconfig(sm)
BuildRequires:	intltool >= 0.35.0
BuildRequires:	itstool 
BuildRequires:	libxml2-utils
Requires:	gstreamer1.0-plugins-good

%description
Goobox is a CD player and ripper that always knows just what to do.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/org.gnome.Goobox.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/metainfo/org.gnome.Goobox.appdata.xml


