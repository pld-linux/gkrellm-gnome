Summary:	GKrellM plugin to use GNOME
Summary(pl):	Plugin gkrellm do u¿ywania z GNOME
Name:		gkrellm-gnome
Version:	0.1
Release:	3
License:	GPL
Vendor:		Bill Wilson <bill@gkrellm.net>
Group:		X11/Applications
Source0:	http://web.wt.net/~billw/gkrellm/Plugins/%{name}.tar.gz
Patch0:		%{name}-CFLAGS.patch
URL:		http://gkrellm.net/
BuildRequires:	gkrellm-devel
BuildRequires:	gnome-libs-devel
Requires:	gkrellm >= 1.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A GKrellM plugin to add GNOME capabilities.

%description -l pl
Plugin GKrellM dodaj±cy mo¿liwo¶ci GNOME.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm

install src/gkrellm-gnome.so $RPM_BUILD_ROOT%{_libdir}/gkrellm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_libdir}/gkrellm/gkrellm-gnome.so
