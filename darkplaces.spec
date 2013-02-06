%define Werror_cflags %nil

Name:		darkplaces
Summary:	Multiplayer, deathmatch oriented first person shooter engine
Version:	rev20110628
Release:	2
License: 	GPLv2+
Group:		Games/Arcade
URL:		http://icculus.org/twilight/darkplaces/
Source:		darkplaces-%{version}.tar.bz2
Patch0:         %{name}-makefile.patch
BuildRequires:	imagemagick file lzma
BuildRequires:	SDL-devel GL-devel unzip jpeg-devel libxxf86dga-devel
BuildRequires:	libalsa-devel libxpm-devel zlib-devel libvorbis-devel
Requires:	zlib libvorbis curl 
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
# Install the main programs
%{__mkdir_p} %{buildroot}%{_gamesbindir}
%{__install} -m 0755 darkplaces-glx \
	%{buildroot}%{_gamesbindir}/darkplaces-glx
%{__install} -m 0755 darkplaces-sdl \
	%{buildroot}%{_gamesbindir}/darkplaces-sdl
%{__install} -m 0755 darkplaces-dedicated \
	%{buildroot}%{_gamesbindir}/darkplaces-dedicated

%files
%defattr(-,root,root,-)
%doc COPYING darkplaces.txt
%{_gamesbindir}/darkplaces-glx
%{_gamesbindir}/darkplaces-sdl

%files server
%defattr(-,root,root,-)
%doc COPYING darkplaces.txt
%{_gamesbindir}/darkplaces-dedicated



%changelog
* Wed Jul 04 2012 Zombie Ryushu <ryushu@mandriva.org> rev20110628-1.1
+ Revision: 808054
- zlib-devel one more time
- libxxf86dga-devel
- libjpeg62-devel
- libjpeg62-devel
- libalsa was wrong
- libvorbis-devel
- zlib-devel was in requires
- vorbis-devel
- vorbis-devel
- zlib
- Upgrade to 4.21 to fix OpenAL and zlib
- Upgrade to rev20110628 for joypad support

* Sun Dec 25 2011 Zombie Ryushu <ryushu@mandriva.org> rev20091001-1.1
+ Revision: 745129
- libjpeg62

* Sat Dec 24 2011 Zombie Ryushu <ryushu@mandriva.org> rev20091001-1
+ Revision: 745104
- shortcut
- fix libxpm
- imported package darkplaces


* Sat Feb 14 2009 muhammedu@gmail.com
- Initial package based on a previous build
- NOTE: I am the only one you should ask about
-	THIS package! Do not email the others
-	mentioned below!
- Only build darkplaces without nexuiz
* Fri Feb 13 2009 nesnomis@gmail.com
- rebuild for opensuse 11.1
* Wed May 21 2008 claes.backstrom@fsfe.org
- Initial package
