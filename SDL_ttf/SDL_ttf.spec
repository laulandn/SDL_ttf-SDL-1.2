%define name SDL_ttf
%define version 2.0.11.1
%define release 1

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-buildroot
Prefix: %{_prefix}
Packager: Hakan Tandogan <hakan@iconsult.com>
#BuildRequires: SDL-devel
#BuildRequires: freetype-devel

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name}
Requires: SDL-devel

%description devel
This library allows you to use TrueType fonts to render text in SDL
applications.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%{prefix}/lib/lib*.a
%{prefix}/lib/lib*.la
%{prefix}/lib/lib*.so
%{prefix}/include/SDL/
%{prefix}/lib/pkgconfig/*.pc

%changelog
* Wed Jan 19 2000 Sam Lantinga 
- converted to get package information from configure
* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file

