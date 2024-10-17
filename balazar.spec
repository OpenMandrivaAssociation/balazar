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
Url:		https://home.gna.org/oomadness/en/balazar/
# or http://balazar.nekeme.net/
Source0:	http://download.gna.org/balazar/%{oname}-%{version}.tar.bz2
Source10:	%{name}-16.png
Source11:	%{name}-32.png
Source12:	%{name}-48.png

BuildArch: noarch
BuildRequires:	python2-devel
BuildRequires:	pkgconfig(sdl)
Requires:	cerealizer
Requires:	pyogg
Requires:	pyopenal
Requires:	python-imaging
Requires:	pyvorbis
Requires:	soya
Requires:	tofu


%description
A 3D adventure and roleplaying game starring Balazar the photo-mage.


%files
%doc AUTHORS README LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/*.egg-info
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

#----------------------------------------------------------------------------


%prep
%setup -q -n %{oname}-%{version}

%build
python2 ./setup.py build

%install
python2 ./setup.py install --root=%{buildroot}
install -m 644 -D %{SOURCE10} %{buildroot}%{_miconsdir}/%{name}.png
install -m 644 -D %{SOURCE11} %{buildroot}%{_iconsdir}/%{name}.png
install -m 644 -D %{SOURCE12} %{buildroot}%{_liconsdir}/%{name}.png

mkdir %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{oname}.desktop << EOF
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