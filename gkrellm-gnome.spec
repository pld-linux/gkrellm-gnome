%define name		gkrellm-gnome
%define version		0.1
%define release		1
%define prefix		/usr

%define builddir	$RPM_BUILD_DIR/%{name}

Summary: GKrellM plugin to use GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Copyright: GPL
Group: X11/Utilities
Source: %{name}.tar.gz
URL: http://gkrellm.net
Vendor: Bill Wilson <bill@gkrellm.net>
Packager: Troy Engel <tengel@sonic.net>
Requires: gkrellm >= 1.0.4 gnome-libs
BuildRoot: /var/tmp/%{name}-root

%description
A GKrellM plugin to add GNOME capabilities

%prep
rm -rf %{builddir}

%setup -n %{name}
touch `find . -type f`

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{prefix}/share/gkrellm/plugins
install -s -m 755 src/gkrellm-gnome.so $RPM_BUILD_ROOT%{prefix}/share/gkrellm/plugins

%files
%defattr(-,root,root)
%doc COPYRIGHT Changelog README
%{prefix}/share/gkrellm/plugins/gkrellm-gnome.so

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}
