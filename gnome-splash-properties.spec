%define name gnome-splash-properties
%define version 0.3.0
%define release %mkrel 2

Summary: GNOME splash selector
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://tchak13.free.fr/gnome-splash-properties/
Source0: http://tchak13.free.fr/gnome-splash-properties/files/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby-gnome2 ruby-gconf2 ruby-gnomevfs2
BuildRequires: ruby ImageMagick
BuildArch: noarch

%description
This application lets you easily setup splash on GNOME desktop.

%prep
%setup -q

%build
ruby setup.rb config

%install
rm -rf %buildroot
ruby setup.rb install --prefix=$RPM_BUILD_ROOT

# Menu
######




cp data/pixmaps/%{name}.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert data/pixmaps/%{name}.png -geometry 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert data/pixmaps/%{name}.png -geometry 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf %buildroot

%post
%update_menus

%postun
%update_menus

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%doc COPYING
