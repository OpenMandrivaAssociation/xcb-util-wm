# xcb-util-wm is used by vkd3d, which is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define ewmh_major 2
%define icccm_major 4

%define libewmh %mklibname xcb-ewmh %{ewmh_major}
%define libicccm %mklibname xcb-icccm %{icccm_major}
%define develname %mklibname %{name} -d
%define lib32ewmh %mklib32name xcb-ewmh %{ewmh_major}
%define lib32icccm %mklib32name xcb-icccm %{icccm_major}
%define devel32name %mklib32name %{name} -d

%global optflags %{optflags} -O3

Summary:	xcb-util-wm
Name:		xcb-util-wm
Version:	0.4.2
Release:	2
Url:		https://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%name-%{version}.tar.xz
License:	MIT
Group:		System/X11
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xorg-macros)
%if %{with compat32}
BuildRequires:	devel(libxcb-util)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

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
Provides:	xcb-util-wm-devel = %{version}-%{release}
Requires:	%{libewmh} = %{version}-%{release}
Requires:	%{libicccm} = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.9
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.9

%description -n %{develname}
This package includes the development files required to build software against
%{name}.

%if %{with compat32}
%package -n %{lib32ewmh}
Summary:	xcb-ewmh library package (32-bit)
Group:		System/X11

%description -n %{lib32ewmh}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{lib32icccm}
Summary:	xcb-icccm library package (32-bit)
Group:		System/X11

%description -n %{lib32icccm}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{devel32name}
Summary:	xcb-util-wm development headers (32-bit)
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Requires:	%{lib32ewmh} = %{version}-%{release}
Requires:	%{lib32icccm} = %{version}-%{release}

%description -n %{devel32name}
This package includes the development files required to build software against
%{name}.
%endif

%prep
%autosetup -p1
export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32 --with-pic
cd ..
%endif

mkdir build
cd build
%configure --with-pic

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libewmh}
%{_libdir}/libxcb-ewmh.so.%{ewmh_major}*

%files -n %{libicccm}
%{_libdir}/libxcb-icccm.so.%{icccm_major}*

%files -n %{develname}
%doc ChangeLog NEWS README.md
%{_includedir}/xcb/xcb_ewmh.h
%{_includedir}/xcb/xcb_icccm.h
%{_libdir}/libxcb-ewmh.so
%{_libdir}/libxcb-icccm.so
%{_libdir}/pkgconfig/xcb-ewmh.pc
%{_libdir}/pkgconfig/xcb-icccm.pc

%if %{with compat32}
%files -n %{lib32ewmh}
%{_prefix}/lib/libxcb-ewmh.so.%{ewmh_major}*

%files -n %{lib32icccm}
%{_prefix}/lib/libxcb-icccm.so.%{icccm_major}*

%files -n %{devel32name}
%{_prefix}/lib/libxcb-ewmh.so
%{_prefix}/lib/libxcb-icccm.so
%{_prefix}/lib/pkgconfig/xcb-ewmh.pc
%{_prefix}/lib/pkgconfig/xcb-icccm.pc
%endif
