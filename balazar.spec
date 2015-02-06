%define name balazar
%define oname Balazar
%define version 0.3.4
%define release 7

Summary:	A 3D adventure and roleplaying game
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Games/Adventure
Source:		http://download.gna.org/balazar/%oname-%version.tar.bz2
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png
URL:		http://home.gna.org/oomadness/en/balazar/
# or http://balazar.nekeme.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel, SDL-devel
Requires:	soya, python-imaging, pyogg, pyvorbis, pyopenal
Requires:	tofu, cerealizer
#dri:)
#pyrex=0.9.3, cal3d=0.9.1
BuildArch: noarch

%description
A 3D adventure and roleplaying game starring Balazar the photo-mage.

%prep

%setup -q -n %oname-%version

%build
python ./setup.py build

%install
rm -Rf $RPM_BUILD_ROOT

python ./setup.py install --root=$RPM_BUILD_ROOT
install -m 644 -D %{SOURCE10} $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install -m 644 -D %{SOURCE11} $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install -m 644 -D %{SOURCE12} $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{oname}.desktop << EOF
[Desktop Entry]
Name=%{oname}
Comment=%{summary}
Exec=%{_bindir}/%{name} %U
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;AdventureGame;
EOF

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{oname}.desktop
%{_datadir}/*.egg-info
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-6mdv2011.0
+ Revision: 616706
- the mass rebuild of 2010.0 packages

* Wed May 13 2009 Samuel Verschelde <stormi@mandriva.org> 0.3.4-5mdv2010.0
+ Revision: 375479
- fix description (fix #49418)
- fix Licence
- fix desktop file

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.4-4mdv2009.0
+ Revision: 243160
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 05 2007 Emmanuel Andry <eandry@mandriva.org> 0.3.4-2mdv2008.1
+ Revision: 115724
- fix menu entry (bug #35851)
- New version
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sat Jan 06 2007 Olivier Blin <oblin@mandriva.com> 0.3.1-5mdv2007.0
+ Revision: 104991
- use english website URL (John Keller)

* Sat Jan 06 2007 Olivier Blin <oblin@mandriva.com> 0.3.1-4mdv2007.1
+ Revision: 104709
- remove glew dependency, it is not required and libglew is already pulled by soya
- remove dependencies that are already required by soya
- remove python-pyrex dependency, it is not required for balazar to run

* Fri Jan 05 2007 Emmanuel Andry <eandry@mandriva.org> 0.3.1-3mdv2007.1
+ Revision: 104587
- Rebuild for python-pyrex
  package egg-info file

  + Eskild Hustvedt <eskild@mandriva.org>
    - Import balazar

* Mon Aug 28 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.1-2mdv2007.0
- requires pyopenal

* Wed Jul 12 2006 Lenny Cartier <lenny@mandriva.com> 0.3.1-1mdv2007.0
- 0.3.1
- requires cerealizer

* Sun Jun 18 2006 Emmanuel Andry <eandry@mandriva.org> 0.3-1mdv2007.0
- 0.3
- xdg compliant

* Thu Oct 27 2005 Lenny Cartier <lenny@mandriva.com> 0.2-2mdk
- rebuild for latest allegro

* Mon Sep 12 2005 Guillaume Bedot <littletux@mandriva.org> 0.2-1mdk
- New release
- added some requires

* Wed Mar 02 2005 Guillaume Bedot <guillaume.bedot@cegetel.net> 0.1-1mdk
- First Mandrakelinux package

