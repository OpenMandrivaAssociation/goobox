%define name goobox
%define version 3.0.1
%define release 1

Summary: CD player and ripper for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/goobox/%{name}-%{version}.tar.xz
License: GPLv2+
Group: Sound
Url: http://www.gnome.org
BuildRequires: pkgconfig(gstreamer-0.10)
BuildRequires: pkgconfig(libmusicbrainz3)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: scrollkeeper
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: pkgconfig(libexslt)
BuildRequires: pkgconfig(sm)
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

%build
%configure2_5x --disable-schemas-install --disable-scrollkeeper
%make

%install
%makeinstall_std
%find_lang %name --with-gnome

desktop-file-install --vendor="" \
  --add-category="Audio;Player" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%files -f %name.lang
%doc README NEWS AUTHORS ChangeLog
%_bindir/%name
%_datadir/applications/goobox.desktop
%_datadir/%{name}
%_datadir/icons/hicolor/*/apps/%{name}.*
%_datadir/GConf/gsettings/%{name}.convert
%_datadir/glib-2.0/schemas/org.gnome.Goobox.gschema.xml


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 2.2.0-3mdv2011.0
+ Revision: 677722
- rebuild to add gconftool as req

* Wed Apr 20 2011 Funda Wang <fwang@mandriva.org> 2.2.0-2
+ Revision: 656128
- build with libnotify 0.7

* Mon Nov 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.0-1mdv2011.0
+ Revision: 597836
- update to new version 2.2.0

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 2.1.2-2mdv2011.0
+ Revision: 571608
- rebuild for new brasero

* Mon Jul 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.1.2-1mdv2011.0
+ Revision: 551300
- update to new version 2.1.2

* Mon Nov 16 2009 Frederik Himpe <fhimpe@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 466682
- Add libunique-devel BuildRequires
- Update to new version 2.1.1
- BuildRequires brasero-devel now

* Mon Sep 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 450576
- new version
- drop patch

* Sat Aug 08 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.0-3mdv2010.0
+ Revision: 411740
- fix format strings

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-2mdv2009.0
+ Revision: 266944
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Apr 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.0-1mdv2009.0
+ Revision: 196784
- new version
- drop patch

  + Thierry Vignaud <tv@mandriva.org>
    - fix gstreamer0.10-devel BR for x86_64
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.2-1mdv2008.0
+ Revision: 72628
- new version
- patch to make it build

  + Funda Wang <fwang@mandriva.org>
    - New version 1.9.2

* Tue Jun 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.1-1mdv2008.0
+ Revision: 41335
- new version
- drop patch
- drop french translation
- fix deps
- drop legacy menu
- update file list
- Import goobox



* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9.93-9mdv2007.0
- Rebuild with latest dbus

* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.9.93-8mdv2007.0
- new macros
- xdg menu

* Fri Feb 10 2006 Götz Waschk <waschk@mandriva.org> 0.9.93-7mdk
- fix installation

* Thu Jan 26 2006 Götz Waschk <waschk@mandriva.org> 0.9.93-6mdk
- patch for new libnotify

* Wed Jan 25 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.93-5mdk
- rebuild for new libnotify
- use mkrel

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 0.9.93-4mdk
- fix buildrequires

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 0.9.93-3mdk
- depend on dbus-x11

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 0.9.93-2mdk
- update buildrequires

* Mon Nov 21 2005 Götz Waschk <waschk@mandriva.org> 0.9.93-1mdk
- drop patch
- New release 0.9.93

* Wed Sep 21 2005 Götz Waschk <waschk@mandriva.org> 0.9.92-3mdk
- update french translation (bug #15962)

* Tue Sep  6 2005 Götz Waschk <waschk@mandriva.org> 0.9.92-2mdk
- drop prereq
- fix song length bug #16266

* Tue Jul 19 2005 Götz Waschk <waschk@mandriva.org> 0.9.92-1mdk
- New release 0.9.92

* Wed May 11 2005 Götz Waschk <waschk@mandriva.org> 0.9.91-3mdk
- fix buildrequires

* Fri May  6 2005 Götz Waschk <waschk@mandriva.org> 0.9.91-2mdk
- fix build on x86_64

* Tue Apr  5 2005 Götz Waschk <waschk@linux-mandrake.com> 0.9.91-1mdk
- new version

* Mon Mar 07 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.9.90-1mdk
- New release 0.9.90

* Tue Jan 25 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.2-1mdk
- register scrollkeeper files
- add new files
- New release 0.7.2

* Wed Jan 12 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.7.1-1mdk
- New release 0.7.1

* Sun Jan  9 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.7.0-1mdk
- New release 0.7.0

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6.0-2mdk 
- Rebuild with latest howl

* Mon Dec  6 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6.0-1mdk
- fix buildrequires
- New release 0.6.0

* Wed Nov 17 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.5.0-1mdk
- New release 0.5.0

* Tue Nov  9 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.4.0-1mdk
- New release 0.4.0

* Sun Oct 31 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-2mdk
- fix buildrequires

* Sat Oct 30 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.3.0-1mdk
- New release 0.3.0

* Sun Oct 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-2mdk
- fix gconf script

* Tue Oct 19 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-1mdk
- update file list
- New release 0.2.0

* Fri Oct 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.0-1mdk
- initial package
