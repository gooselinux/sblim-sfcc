#
# $Id: sfcc.spec.in,v 1.2 2007/02/27 14:07:00 mihajlov Exp $
#
# Package spec for sblim-sfcc
#

#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXXX)

Summary: Small Footprint CIM Client Library
Name: sblim-sfcc
Version: 2.2.1
Release: 4%{?dist}
Group: Applications/System
License: EPL
URL: http://www.sblim.org
Source0: http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0: sblim-sfcc-2.2.1-release_cimcenv.patch
#Patch1, Patch2: accepted by upstream
Patch1: sblim-sfcc-2.2.1-support-CMPI_chars-in-the-cimxml-backend.patch
Patch2: sblim-sfcc-2.2.1-support-use-of-CMPI_chars-in-sfccclient.c.patch
BuildRequires: curl-devel

%Description
Small Footprint CIM Client Library Runtime Libraries

%package devel
Summary: Small Footprint CIM Client Library
Group: Applications/System
Requires: %{name} = %{version}-%{release}

%Description devel
Small Footprint CIM Client Library Header Files and Link Libraries


%prep

%setup -q
%patch0 -p1 -b .release_cimcenv
%patch1 -p1 -b .support-CMPI_chars-in-the-cimxml-backend
%patch2 -p1 -b .support-use-of-CMPI_chars-in-sfccclient.c

%build
chmod a-x backend/cimxml/*.[ch]

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%configure 
make %{?_smp_flags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

# remove unused libtool files

rm -rf %{buildroot}/%{_libdir}/*a 
%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_mandir}/man3/*.3.gz
%{_docdir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/CimClientLib/*
%{_includedir}/cimc/*
%{_libdir}/*.so 

%changelog
* Wed Jun 16 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-4
- Fix sblim-sfcc-devel requires
- Add -fno-strict-aliasing

* Wed May 26 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-3
- Prefer CMPI_chars over CMPI_classNameString

* Tue May 18 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-2
- Fix release CIMCEnv on client connection error

* Thu Mar 11 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-1
- Update to sblim-sfcc-2.2.1

* Tue Mar  2 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.0-4
- Fix Source field
- Move documentation files from -devel to main package

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1.0-3.1
- Rebuilt for RHEL 6

* Fri Oct  2 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 2.1.0-3
- Added a patch to prevent crash because of uninitialized structrues.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 19 2008  <srinivas_ramanatha@dell.com> - 2.1.0-0%{?dist}
- Modified the spec file to adhere to fedora packaging guidelines.

* Fri Feb 16 2007  <mihajlov@dyn-9-152-143-45.boeblingen.de.ibm.com> - 2.0.0-0
- Initial Version

