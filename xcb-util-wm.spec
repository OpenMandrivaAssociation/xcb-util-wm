%define ewmh_major 2
%define icccm_major 4

%define libewmh %mklibname xcb-ewmh %{ewmh_major}
%define libicccm %mklibname xcb-icccm %{icccm_major}
%define develname %mklibname %{name} -d
%define develnamest %mklibname %{name} -d -s

Summary:	xcb-util-wm
Name:		xcb-util-wm
Version:	0.3.9
Release:	5
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%name-%{version}.tar.bz2
License:	MIT
Group:		System/X11
BuildRequires:	xcb-util-devel >= 0.3.9
BuildRequires:	x11-util-macros

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{libewmh}
Summary:	xcb-ewmh library package
Group:		System/X11

%description -n %{libewmh}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{libicccm}
Summary:	xcb-icccm library package
Group:		System/X11

%description -n %{libicccm}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{develname}
Summary:	xcb-util-wm development headers
Group:		Development/C
Provides:	libxcb-util-wm-devel = %{version}-%{release}
Provides:	xcb-util-wm-devel = %{version}-%{release}
Requires:	%{libewmh} = %{version}-%{release}
Requires:	%{libicccm} = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.9
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.9

%description -n %{develname}
This package includes the development files required to build software against
%{name}.

%package -n %{develnamest}
Summary:	xcb-util-wm development static files
Group:		Development/C
Provides:	libxcb-util-wm-devel-static = %{version}-%{release}
Provides:	xcb-util-wm-devel-static = %{version}-%{release}
Requires:	%{libewmh} = %{version}-%{release}
Requires:	%{libicccm} = %{version}-%{release}
Requires:	xcb-util-wm-devel = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.9
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.9

%description -n %{develnamest}
This package includes the static development
files required to build software against
%{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libewmh}
%{_libdir}/libxcb-ewmh.so.%{ewmh_major}*

%files -n %{libicccm}
%{_libdir}/libxcb-icccm.so.%{icccm_major}*

%files -n %{develnamest}
%{_libdir}/libxcb-ewmh.a
%{_libdir}/libxcb-icccm.a

%files -n %{develname}
%doc ChangeLog NEWS README
%{_includedir}/xcb/xcb_ewmh.h
%{_includedir}/xcb/xcb_icccm.h
%{_libdir}/libxcb-ewmh.so
%{_libdir}/libxcb-icccm.so
%{_libdir}/pkgconfig/xcb-ewmh.pc
%{_libdir}/pkgconfig/xcb-icccm.pc


%changelog
* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.9-1
+ Revision: 802328
- version update 0.3.9

* Wed Oct 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8-1
+ Revision: 707434
- import xcb-util-wm

