# $Id: id3lib.spec,v 1.2 2000-06-09 07:22:59 kloczek Exp $

Name:		id3lib
Version:	3.7.9
Release:	1
Summary:	A software library for manipulating ID3v1 and ID3v2 tags.
Source0:	http://download.sourceforge.net/id3lib/%{name}-%{version}.tar.gz
URL:		http://id3lib.sourceforge.net
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	LGPL
Requires:	zlib

%description
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities.

%package	devel
Summary:	Headers for developing programs that will use id3lib
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}

%description	devel
This package contains the headers that programmers will need to
develop applications which will use id3lib, the software library for
ID3v1 and ID3v2 tag manipulation.

%package        doc
Summary:	Documentation for developing programs that will use id3lib
Group:		Documentation
Group(pl):	Dokumentacja

%description	doc
This package contains the documentation of the id3lib API that
programmers will need to develop applications which will use id3lib,
the software library for ID3v1 and ID3v2 tag manipulation.

%package        examples
Summary:	Example applications that make use of the id3lib library
Group:		Applications/File
######		Unknown group!
Requires:	%{name}

%description	examples
This package contains simple example applications that make use of
id3lib, a software library for ID3v1 and ID3v2 tag maniuplation.

%prep
%setup -q

%build
%ifarch i386 i486
ID3_ARCH=i486
%endif 

%ifarch i586
ID3_ARCH=pentium
%endif 

%ifarch i686
ID3_ARCH=pentiumpro
%endif 

%ifarch k6
ID3_ARCH=k6
%endif

%ifarch i386 i486 i586 i686 k6

RPM_OPT_FLAGS="-O3 -fomit-frame-pointer -pipe -s -mcpu=$ID3_ARCH -march=$ID3_ARCH -ffast-math -fexpensive-optimizations -malign-loops=2 -malign-jumps=2 -malign-functions=2 -mpreferred-stack-boundary=2"

%endif

CXXFLAGS="$RPM_OPT_FLAGS -fexceptions" %configure

%ifnarch noarch

uname -a|grep SMP && make -j 2 || make

%endif

%install
rm -rf $RPM_BUILD_ROOT

%ifnarch noarch

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%else

%{__make} docs
 
# strip down the doc and examples directories so we can copy w/impunity
for i in doc/ examples/; do \
  find $i                   \
  \(  -name 'Makefile*' -or \
      -name '*.ps.gz'   -or \
      -name '*.pdf'         \
  \)  -exec rm {} \; ; done

%endif

gzip -9nf AUTHORS ChangeLog HISTORY NEWS README THANKS TODO


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%ifnarch noarch

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,HISTORY,NEWS,README,THANKS,TODO}.gz
%{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/id3*.h
%{_includedir}/id3
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/id3*

%else

%files doc
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog HISTORY NEWS README THANKS TODO
%doc doc/*.* doc/api examples

%endif
