%define	major	1
%define api_version 1.0
%define	libname	%mklibname openraw %{major}
%define	devname	%mklibname -d openraw
%define	libgnm	%mklibname openrawgnome %{major}

Summary:	Camera RAW files decoding library
Name:		libopenraw
Version:	0.0.9
Release:	2
License:	LGPLv3+
Group:		Graphics
Source0: 	http://libopenraw.freedesktop.org/download/%name-%version.tar.bz2
Url:		http://libopenraw.freedesktop.org
BuildRequires:	jpeg-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libcurl)
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
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d openraw 1
Group:		Development/C

%description -n	%{devname}
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
%makeinstall_std

%files
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so

%files -n %{libname} 
%doc AUTHORS NEWS README ChangeLog TODO
%{_libdir}/libopenraw.so.%{major}*

%files -n %{libgnm} 
%{_libdir}/libopenrawgnome.so.%{major}*

%files -n %{devname}
%doc doc/doxygen/html/
%{_includedir}/libopenraw-%{api_version}
%{_libdir}/libopenraw.so
%{_libdir}/libopenrawgnome.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Feb 12 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.0.9-2
- add buildrequires on pkgconfig(libcurl)
- split out libopenrawgnome into separate library package
- cosmetics
- use pkgconfig() deps for buildrequires

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
