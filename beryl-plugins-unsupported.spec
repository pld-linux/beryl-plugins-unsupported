Summary:	beryl plugins
Summary(pl):	Wtyczki do beryla
Name:		beryl-plugins-unsupported
Version:	0.1.9999.1
Release:	1
License:	GPL
Group:		X11
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	76fb0088c25c3b8171a54ad16ef702e8
URL:		http://beryl-project.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	cairo-devel >= 1.0
BuildRequires:	dbus-devel >= 0.50
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	librsvg-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	beryl-core >= 1:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beryl extra plugins.

This package contains plugins that are either:
- unstable
- only modestly maintained
- or completely unmaintained

Use at your own risk.

%description -l pl
Dodatkowe wtyczki do beryla.

Ten pakiet zawiera wtyczki które:
- s± niestabilne,
- nie maj± zapewnionej dostatecznej opieki,
- lub którymi nikt siê nie zajmuje.

Do u¿ytku tylko na w³asne ryzyko.

%prep
%setup -q

mv -f po/{es_ES,es}.po
mv -f po/{ko_KR,ko}.po
cat > po/LINGUAS <<EOF
es
ko
nl
EOF

%build
%{__glib_gettextize}
%{__intltoolize} --automake
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/beryl/*.la

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/beryl/*.so
