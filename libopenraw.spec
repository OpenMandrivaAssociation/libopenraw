%define major	1
%define api_version 1.0
%define libname	%mklibname openraw %{major}
%define develname %mklibname -d openraw

Summary:	Camera RAW files decoding library
Name:		libopenraw
Version:	0.0.4
Release:	%mkrel 1
License:	LGPLv2+
Group:		Graphics
Source: 	http://libopenraw.freedesktop.org/download/%name-%version.tar.gz
Url:		http://libopenraw.freedesktop.org
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	jpeg-devel boost-devel glib2-devel libgdk_pixbuf2.0-devel
BuildRequires:	libxml2-devel
BuildRequires:	doxygen
BuildRequires:	autoconf

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
Group:		Graphics

%description -n %{libname}
libopenraw is an ongoing project to provide a free software implementation 
for camera RAW files decoding. One of the main reason is that dcraw is not 
suited for easy integration into applications, and there is a need for an
easy to use API to build free software digital image processing application.

It also has the goal to address missing feature from dcraw like meta-data 
decoding and easy thumbnail extraction.

%package -n %{develname}
Summary:	Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d openraw 1
Group:		Graphics

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q 
sed -i -e 's|@top_srcdir@/dcraw ||' doc/Doxyfile.in

%build
%configure2_5x 
%make
make dox

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname} 
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc AUTHORS NEWS COPYING README ChangeLog TODO

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/libopenraw-%{api_version}
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc doc/doxygen/html/
