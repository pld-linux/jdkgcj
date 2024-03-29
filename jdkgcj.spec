Summary:	A free Java SDK
Summary(pl.UTF-8):	Wolnodostępne SDK dla Javy
Name:		jdkgcj
Version:	0.3.1
Release:	3
License:	GPL v2
Group:		Development/Languages
Source0:	http://www.arklinux.org/projects/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	850fd5b28d3338457e910e900b2b4dbe
URL:		http://freshmeat.net/projects/jdkgcj/
BuildRequires:	gcc-java >= 5:3.3.3-1
Requires:	gcc-java >= 5:3.3.3-1
Requires:	libgcj-devel >= 5:3.3.3-1
Provides:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jdkgcj provides an interface to gcj that is compatible with the Sun
and IBM Java Development Kits (JDKs). jdkgcj provides the javac, java
and javah tools.

%description -l pl.UTF-8
jdkgcj dostarcza interfejs do gcj kompatybilny z pakietami JDK (Java
Development Kit) od Suna i IBM-a. jdkgcj dostarcza narzędzia javac,
java i javah.

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
