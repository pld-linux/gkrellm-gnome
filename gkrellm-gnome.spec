Summary:	GKrellM plugin to use GNOME
Name:		gkrellm-gnome
Version:	0.1
Release:	2
License:	GPL
Vendor:		Bill Wilson <bill@gkrellm.net>
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://web.wt.net/~billw/gkrellm/Plugins/%{name}.tar.gz
Patch0:		%{name}-CFLAGS.patch
URL:		http://gkrellm.net/
BuildRequires:	gkrellm-devel
BuildRequires:	gnome-libs-devel
Requires:	gkrellm >= 1.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A GKrellM plugin to add GNOME capabilities.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make} CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm

install src/gkrellm-gnome.so $RPM_BUILD_ROOT%{_libdir}/gkrellm

gzip -9nf Changelog README

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gkrellm/gkrellm-gnome.so

%clean
rm -rf $RPM_BUILD_ROOT
