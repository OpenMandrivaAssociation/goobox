%define url_ver %(echo %{version} | cut -d. -f1,2)
%define gstapi	0.10

Summary:	CD player and ripper for GNOME
Name: 		goobox
Version:	3.0.1
Release:	1
License:	GPLv2+
Group:		Sound
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goobox/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libbrasero-media3)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libmusicbrainz3)
BuildRequires:	pkgconfig(libnotify)
Requires:	gstreamer%{gstapi}-plugins-good
Requires:	dbus-x11

%description
Goobox is a CD player and ripper that always knowns just what to do.

%prep
%setup -q

%build
%configure2_5x \
	--disable-schemas-install \
	--disable-scrollkeeper
%make

%install
%makeinstall_std
%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
	--add-category="Audio;Player" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*


%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/goobox.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Goobox.gschema.xml

