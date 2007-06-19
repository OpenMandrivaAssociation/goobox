%define name goobox
%define version 0.9.93
%define release %mkrel 9

Summary: CD player and ripper for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/goobox/%{name}-%{version}.tar.bz2
Source1: goobox-0.9.92-fr.po.bz2
Patch: goobox-0.9.93-libnotify.patch.bz2
License: GPL
Group: Sound
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gstreamer-plugins-devel
BuildRequires: libgnomeui2-devel >= 2.6
BuildRequires: libglade2.0-devel
BuildRequires: libnotify-devel >= 0.3.0
BuildRequires: scrollkeeper
BuildRequires: perl-XML-Parser
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
#if patched
BuildRequires: intltool
Requires: gstreamer-cdparanoia
Requires: gstreamer-vorbis
Requires: dbus-x11
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
Goobox is a CD player and ripper that always knowns just what to do.

%prep
%setup -q
%patch -p1
bzcat %SOURCE1 > po/fr.po

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std _ENABLE_SK=no
%find_lang %name --with-gnome
mkdir -p $RPM_BUILD_ROOT/%{_menudir}
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" icon="%{name}.png" \
  needs="x11" section="Multimedia/Sound" title="Goobox" \
  longtitle="Play and extract CDs" startup_notify="true" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p $RPM_BUILD_ROOT/{%{_miconsdir},%_liconsdir}
ln -s %_datadir/pixmaps/%name.png %buildroot%_liconsdir/
convert -scale 32 data/%name.png %buildroot%_iconsdir/%name.png
convert -scale 16 data/%name.png %buildroot%_miconsdir/%name.png

rm -rf %buildroot/var

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper
%post_install_gconf_schemas %name
%update_menus

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_scrollkeeper
%clean_menus


%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/%name
%_libdir/bonobo/servers/GNOME_Goobox.server
%_datadir/application-registry/goobox.applications
%_datadir/applications/goobox.desktop
%_datadir/%name
%_datadir/pixmaps/%name.png
%dir %_datadir/omf/%name/
%_datadir/omf/%name/%name-C.omf
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
%_menudir/%name
