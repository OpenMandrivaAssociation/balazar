%define name balazar
%define oname Balazar
%define version 0.3.4
%define release %mkrel 6

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


