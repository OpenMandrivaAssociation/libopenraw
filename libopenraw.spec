%define major	1
%define api_version 1.0
%define libname	%mklibname openraw %{major}
%define develname %mklibname -d openraw

Summary:	Camera RAW files decoding library
Name:		libopenraw
Version:	0.0.9
Release:	1
License:	LGPLv3+
Group:		Graphics
Source0: 	http://libopenraw.freedesktop.org/download/%name-%version.tar.bz2
Url:		http://libopenraw.freedesktop.org
BuildRequires:	jpeg-devel
BuildRequires:	boost-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libxml2-devel
BuildRequires:	doxygen
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
sed -i -e 's|@top_srcdir@/dcraw ||' doc/Doxyfile.in

%build
%configure2_5x --disable-static
%make
make dox

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so

%files -n %{libname} 
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*
%doc AUTHORS NEWS COPYING README ChangeLog TODO

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/libopenraw-%{api_version}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc doc/doxygen/html/


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.8-5mdv2011.0
+ Revision: 660273
- mass rebuild

* Thu Jul 29 2010 Funda Wang <fwang@mandriva.org> 0.0.8-4mdv2011.0
+ Revision: 563212
- add patch to build correctly with gdk 2.22

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.8-3mdv2010.1
+ Revision: 488780
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.0.8-2mdv2010.0
+ Revision: 416623
- rebuilt against libjpeg v7

* Sat May 16 2009 Götz Waschk <waschk@mandriva.org> 0.0.8-1mdv2010.0
+ Revision: 376363
- update to new version 0.0.8

* Sat May 02 2009 Frederik Himpe <fhimpe@mandriva.org> 0.0.7-1mdv2010.0
+ Revision: 370808
- Don't build static libraries
- Remove glib2-devel BuildRequires, already required by libgdk_pixbuf2.0-devel
- Add gtk+2-devel BuildRequires in order to build gdkpixbufloaders
- Put gdkpixbufloaders in libopenraw package instead of in devel package
- update to new version 0.0.7

  + Emmanuel Andry <eandry@mandriva.org>
    - BR curl-devel
    - New version 0.0.6
    - license is now LGPLv3+

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.0.5-3mdv2009.0
+ Revision: 222945
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 23 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.5-2mdv2008.1
+ Revision: 189603
- Fix groups
- protect major

* Tue Feb 26 2008 Götz Waschk <waschk@mandriva.org> 0.0.5-1mdv2008.1
+ Revision: 175263
- new version

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 0.0.4-1mdv2008.1
+ Revision: 158880
- BR libxml2
- New version 0.0.4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Feb 19 2007 Pascal Terjan <pterjan@mandriva.org> 0.0.2-1mdv2007.0
+ Revision: 122750
- Import libopenraw

* Mon Feb 19 2007 Pascal Terjan <pterjan@mandriva.org> 0.0.2-1mdv2007.1
- Initial release

