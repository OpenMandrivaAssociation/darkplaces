%define Werror_cflags %nil

%define debug_package %{nil}

Summary:	Multiplayer, deathmatch oriented first person shooter engine
Name:		darkplaces
Version:	20130304
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Games/Arcade
Url:		http://icculus.org/twilight/darkplaces/
Source0:	%{name}enginesource%{version}.zip
# Debian patchset
Patch0:		0001-Split-Unix-CFLAGS-libs-to-one-per-line.patch
Patch1:		0002-Add-support-for-make-LINK_TO_LIBJPEG-1.patch
Patch2:		0003-Add-support-for-make-LINK_TO_ZLIB-1.patch
Patch3:		0004-Add-support-for-LINK_TO_LIBVORBIS-using-pkg-config.patch
Patch4:		0005-Add-LINK_TO_MODPLUG-option.patch
Patch5:		0006-add-LINK_TO_ODE-to-link-against-system-libode.patch
Patch6:		0007-add-LINK_TO_THEORA.patch
Patch7:		0008-Add-LINK_TO_PNG.patch
Patch8:		0009-add-LINK_TO_CURL.patch
Patch9:		0010-Add-LINK_TO_FREETYPE2.patch
Patch10:	0011-Add-support-for-linking-to-system-d0_blind_id-and-d0.patch
Patch11:	0012-Add-support-for-forcing-d0_blind_id-and-d0_rijndael-.patch
Patch12:	0014-image_png.h-change-name-of-multiple-inclusion-guard-.patch
Patch13:	0015-Be-more-type-safe-when-calling-setjmp-call-the-same-.patch
Patch14:	0016-Be-a-bit-more-type-safe-about-using-libpng.patch
Patch15:	0017-Fix-various-typos-dont-don-t-doesnt-doesn-t-arguemen.patch
Patch16:	0018-Don-t-build-SSE-only-software-rasterizer-on-non-x86-.patch
Patch17:	0019-If-linking-libpng-conventionally-use-the-png_jmpbuf-.patch
Patch18:	0020-If-linking-libpng-normally-use-its-header-to-get-the.patch
Patch19:	0021-If-linking-libpng-in-the-normal-way-use-its-actual-v.patch
Patch20:	0022-Add-support-for-disabling-libavw.patch
Patch21:	0023-Disable-dlopen-support-and-warn-if-it-gets-compiled-.patch
Patch22:	0024-Disable-gpu-skinning-for-skeletal-models.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ode)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	pkgconfig(zlib)
Requires:	curl

%description
Darkplaces is a modern, powerful first-person shooter engine.

%files
%doc COPYING darkplaces.txt
%{_gamesbindir}/darkplaces-glx
%{_gamesbindir}/darkplaces-sdl

#----------------------------------------------------------------------------

%package server
Summary:	Dedicated server for the darkplaces engine
Group:		Games/Arcade
Requires:	curl

%description server
Darkplaces is a modern, powerful first-person shooter engine.

This is the darkplaces dedicated server required to host network games.

%files server
%doc COPYING darkplaces.txt
%{_gamesbindir}/darkplaces-dedicated

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%autopatch -p1

%build
make \
	release \
	OPTIM_RELEASE="%{optflags}" \
	LINK_TO_CURL=1 \
	LINK_TO_FREETYPE2=1 \
	LINK_TO_LIBJPEG=1 \
	LINK_TO_LIBVORBIS=1 \
	LINK_TO_MODPLUG=1 \
	LINK_TO_ODE=1 \
	LINK_TO_PNG=1 \
	LINK_TO_THEORA=1 \
	LINK_TO_ZLIB=1 \
	DISABLE_OFFSCREEN_GECKO=1 \
	DISABLE_D0_BLIND_ID=1 \
	DISABLE_D0_RIJNDAEL=1

%install
# Install the main programs
mkdir -p %{buildroot}%{_gamesbindir}
install -m 0755 darkplaces-glx \
	%{buildroot}%{_gamesbindir}/darkplaces-glx
install -m 0755 darkplaces-sdl \
	%{buildroot}%{_gamesbindir}/darkplaces-sdl
install -m 0755 darkplaces-dedicated \
	%{buildroot}%{_gamesbindir}/darkplaces-dedicated

