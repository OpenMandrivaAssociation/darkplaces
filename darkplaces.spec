%define Werror_cflags %nil

Name:		darkplaces
Summary:	Multiplayer, deathmatch oriented first person shooter engine
Version:	rev20091001
Release:	%mkrel 1
License: 	GPLv2+
Group:		Games/Arcade
URL:		http://icculus.org/twilight/darkplaces/
Source:		darkplaces-rev20091001.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build
BuildRequires:	ImageMagick file lzma
BuildRequires:	SDL-devel GL-devel unzip
BuildRequires:	alsa-lib-devel libxpm-devel
Requires:	zlib libvorbis libjpeg curl
Provides:	nexuiz-engine = 242

%description
Darkplaces is a modern, powerful first-person shooter engine.

This package is non-free as it requires non-free data to run. You must have a version of Quake 1 to play.

%package server
Group: Games/Arcade
Summary: Dedicated server for the darkplaces engine
Requires: 	zlib curl
Provides: 	nexuiz-engine = 242

%description server
Darkplaces is a modern, powerful first-person shooter engine.

This is the darkplaces dedicated server required to host network games.


%prep
%setup -q

%build
%{__make} release OPTIM_RELEASE="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}


# Install the main programs
%{__mkdir_p} %{buildroot}%{_gamesbindir}
%{__install} -m 0755 darkplaces-glx \
	%{buildroot}%{_gamesbindir}/darkplaces-glx
%{__install} -m 0755 darkplaces-sdl \
	%{buildroot}%{_gamesbindir}/darkplaces-sdl
%{__install} -m 0755 darkplaces-dedicated \
	%{buildroot}%{_gamesbindir}/darkplaces-dedicated

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING darkplaces.txt
%{_gamesbindir}/darkplaces-glx
%{_gamesbindir}/darkplaces-sdl

%files server
%defattr(-,root,root,-)
%doc COPYING darkplaces.txt
%{_gamesbindir}/darkplaces-dedicated

