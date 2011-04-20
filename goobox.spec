%define name goobox
%define version 2.2.0
%define release %mkrel 2

Summary: CD player and ripper for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/goobox/%{name}-%{version}.tar.bz2
Patch0: http://www.nyx.net/~amunkres/goobox/goobox-2.2.0-libnotify-0.7.patch
License: GPLv2+
Group: Sound
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gstreamer0.10-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: libgnomeui2-devel >= 2.6
BuildRequires: libglade2.0-devel
BuildRequires: libnotify-devel >= 0.3.0
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: brasero-devel
BuildRequires: unique-devel
Requires: gstreamer0.10-plugins-good
Requires: dbus-x11

%description
Goobox is a CD player and ripper that always knowns just what to do.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-schemas-install --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

desktop-file-install --vendor="" \
  --add-category="Audio;Player" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


rm -rf %buildroot/var

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_scrollkeeper
%post_install_gconf_schemas %name
%update_menus
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas %name

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/%name
%_datadir/applications/goobox.desktop
%_datadir/%name
%_datadir/icons/hicolor/*/apps/goobox.*
%dir %_datadir/omf/%name/
%_datadir/omf/%name/%name-C.omf
