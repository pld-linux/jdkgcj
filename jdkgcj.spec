Summary:	A free Java SDK
Name:		jdkgcj
Version:	0.3.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.arklinux.org/projects/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.arklinux.org/projects/jdkgcj
BuildRequires:	gcc-java >= 3.2
Requires:	gcc-java >= 3.2
Requires:	libgcj >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jdkgcj provides an interface to gcj that is compatible with the Sun
and IBM Java Development Kits (JDKs). jdkgcj provides the javac, java
and javah tools as well as jni.h, allowing you to compile java
extensions using JNI.

%prep
%setup -q -n %{name}

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
