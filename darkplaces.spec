%define Werror_cflags %nil

Name:		darkplaces
Summary:	Multiplayer, deathmatch oriented first person shooter engine
Version:	rev20110628
Release:	%mkrel 1.1
License: 	GPLv2+
Group:		Games/Arcade
URL:		http://icculus.org/twilight/darkplaces/
Source:		darkplaces-%{version}.tar.bz2
Patch0:         %{name}-makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build
BuildRequires:	imagemagick file lzma
BuildRequires:	SDL-devel GL-devel unzip
BuildRequires:	alsa-lib-devel libxpm-devel
Requires:	zlib libvorbis libjpeg62 curl zlib-devel vorbis-devel
Provides:	nexuiz-engine = 242

%description
Darkplaces is a modern, powerful first-person shooter engine.

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
%patch0 -p1

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

