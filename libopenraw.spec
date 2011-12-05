%define major	1
%define api_version 1.0
%define libname	%mklibname openraw %{major}
%define develname %mklibname -d openraw

%define build_dox 0

Summary:	Camera RAW files decoding library
Name:		libopenraw
Version:	0.0.9
Release:	1
License:	LGPLv3+
Group:		Graphics
Url:		http://libopenraw.freedesktop.org
Source0: 	http://libopenraw.freedesktop.org/download/%name-%version.tar.bz2

BuildRequires:	jpeg-devel
BuildRequires:	boost-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxml2-devel
%if %{build_dox}
BuildRequires:	doxygen
%endif
Requires(post):	gdk-pixbuf2.0
Requires(postun): gdk-pixbuf2.0

%description
libopenraw is an ongoing project to provide a free software implementation
for camera RAW files decoding. One of the main reason is that dcraw is not
suited for easy integration into applications, and there is a need for an
easy to use API to build free software digital image processing application.

It also has the goal to address missing feature from dcraw like meta-data
decoding and easy thumbnail extraction. 

%package -n %{libname}
Summary:	Camera RAW files decoding library
Provides:	%{name} = %{version}-%{release}
Group:		System/Libraries

%description -n %{libname}
libopenraw is an ongoing project to provide a free software implementation 
for camera RAW files decoding. One of the main reason is that dcraw is not 
suited for easy integration into applications, and there is a need for an
easy to use API to build free software digital image processing application.

It also has the goal to address missing feature from dcraw like meta-data 
decoding and easy thumbnail extraction.

%package -n %{develname}
Summary:	Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d openraw 1
Group:		Development/C

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q 
%if %{build_dox}
sed -i -e 's|@top_srcdir@/dcraw ||' doc/Doxyfile.in
%endif

%build
%configure2_5x \
	--disable-static

%make

%if %{build_dox}
make dox
%endif

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la | xargs rm

%files
%doc AUTHORS NEWS COPYING README ChangeLog TODO
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so

%files -n %{libname} 
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/libopenraw-%{api_version}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%if %{build_dox}
%doc doc/doxygen/html/
%endif
