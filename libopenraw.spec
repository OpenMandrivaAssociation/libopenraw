%define major 7
%define api 0.1
%define libname %mklibname openraw %{major}
%define devname %mklibname -d openraw
%define libgnm %mklibname openrawgnome %{major}

%define _disable_rebuild_configure 1

Summary:	Camera RAW files decoding library
Name:		libopenraw
Version:	0.1.3
Release:	1
License:	LGPLv3+
Group:		Graphics
Url:		http://libopenraw.freedesktop.org
Source0: 	http://libopenraw.freedesktop.org/download/%name-%version.tar.bz2

BuildRequires:	doxygen
BuildRequires:	jpeg-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libcurl)
Requires(post):	gdk-pixbuf2.0
Requires(postun): gdk-pixbuf2.0

%description
libopenraw is an ongoing project to provide a free software implementation
for camera RAW files decoding. One of the main reason is that dcraw is not
suited for easy integration into applications, and there is a need for an
easy to use API to build free software digital image processing application.

It also has the goal to address missing feature from dcraw like meta-data
decoding and easy thumbnail extraction. 

%package -n	%{libname}
Summary:	Camera RAW files decoding library
Provides:	%{name} = %{version}-%{release}
Group:		System/Libraries

%description -n	%{libname}
libopenraw is an ongoing project to provide a free software implementation 
for camera RAW files decoding. One of the main reason is that dcraw is not 
suited for easy integration into applications, and there is a need for an
easy to use API to build free software digital image processing application.

It also has the goal to address missing feature from dcraw like meta-data 
decoding and easy thumbnail extraction.

%package -n	%{libgnm}
Summary:	Camera RAW files decoding library for GNOME
Provides:	%{name} = %{version}-%{release}
Group:		System/Libraries
Conflicts:	%{libname} < 0.0.9-2

%description -n	%{libgnm}
libopenraw is an ongoing project to provide a free software implementation 
for camera RAW files decoding. One of the main reason is that dcraw is not 
suited for easy integration into applications, and there is a need for an
easy to use API to build free software digital image processing application.

It also has the goal to address missing feature from dcraw like meta-data 
decoding and easy thumbnail extraction.

%package -n	%{devname}
Summary:	Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Requires:	%{libgnm} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q 
sed -i -e 's|@top_srcdir@/dcraw ||' doc/Doxyfile.in

%build
%configure
%make
make dox

%install
%makeinstall_std

%files
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so

%files -n %{libname} 
%{_libdir}/libopenraw.so.%{major}*

%files -n %{libgnm} 
%{_libdir}/libopenrawgnome.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README TODO
%doc doc/doxygen/html/
%{_includedir}/libopenraw-%{api}
%{_libdir}/libopenraw.so
%{_libdir}/libopenrawgnome.so
%{_libdir}/pkgconfig/*.pc
