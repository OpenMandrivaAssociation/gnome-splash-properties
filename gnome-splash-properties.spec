%define name gnome-splash-properties
%define version 0.3.0
%define release 8

Summary: GNOME splash selector
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://tchak13.free.fr/gnome-splash-properties/
Source0: http://tchak13.free.fr/gnome-splash-properties/files/%{name}-%{version}.tar.bz2
Patch0:	gnome-splash-properties-0.3.0-current_folder_uri.patch
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby-gnome2 ruby-gconf2 ruby-gnomevfs2
BuildRequires: ruby imagemagick
BuildArch: noarch

%description
This application lets you easily setup splash on GNOME desktop.

%prep
%setup -q
%patch0 -p0

%build
ruby setup.rb config

%install
rm -rf %buildroot
mkdir -p %buildroot/
ruby setup.rb install --prefix=$RPM_BUILD_ROOT

# Menu
######

mkdir -p $RPM_BUILD_ROOT%{_liconsdir} $RPM_BUILD_ROOT%{_iconsdir} $RPM_BUILD_ROOT%{_miconsdir}
cp data/pixmaps/%{name}.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert data/pixmaps/%{name}.png -geometry 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert data/pixmaps/%{name}.png -geometry 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%doc COPYING


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-7mdv2011.0
+ Revision: 619113
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-6mdv2010.0
+ Revision: 437786
- rebuild

* Tue Mar 03 2009 Pascal Terjan <pterjan@mandriva.org> 0.3.0-5mdv2009.1
+ Revision: 347790
- Fix a runtime crash
- Fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jun 25 2007 Pascal Terjan <pterjan@mandriva.org> 0.3.0-2mdv2008.0
+ Revision: 43993
- set "xdg=true"
- Import gnome-splash-properties



* Wed Nov 16 2005 Pascal Terjan <pterjan@mandriva.org> 0.3.0-1mdk
- 0.3.0

* Sat Nov 12 2005 Pascal Terjan <pterjan@mandriva.org> 0.2.1-1mdk
- 0.2.1

* Sat Nov 12 2005 Pascal Terjan <pterjan@mandriva.org> 0.2.0-1mdk
- first mdk release
