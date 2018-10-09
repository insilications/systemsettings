#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x11968C44928CAEFC (bhush94@gmail.com)
#
Name     : systemsettings
Version  : 5.14.0
Release  : 6
URL      : https://download.kde.org/stable/plasma/5.14.0/systemsettings-5.14.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.0/systemsettings-5.14.0.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.0/systemsettings-5.14.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: systemsettings-bin
Requires: systemsettings-lib
Requires: systemsettings-data
Requires: systemsettings-license
Requires: systemsettings-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev
BuildRequires : kactivities-stats-dev
BuildRequires : kcmutils-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdeclarative-dev
BuildRequires : khtml-dev
BuildRequires : kirigami2-dev
BuildRequires : kjs-dev
BuildRequires : kpackage-dev
BuildRequires : kwindowsystem-dev
BuildRequires : plasma-workspace-dev

%description
No detailed description available

%package bin
Summary: bin components for the systemsettings package.
Group: Binaries
Requires: systemsettings-data = %{version}-%{release}
Requires: systemsettings-license = %{version}-%{release}

%description bin
bin components for the systemsettings package.


%package data
Summary: data components for the systemsettings package.
Group: Data

%description data
data components for the systemsettings package.


%package dev
Summary: dev components for the systemsettings package.
Group: Development
Requires: systemsettings-lib = %{version}-%{release}
Requires: systemsettings-bin = %{version}-%{release}
Requires: systemsettings-data = %{version}-%{release}
Provides: systemsettings-devel = %{version}-%{release}

%description dev
dev components for the systemsettings package.


%package doc
Summary: doc components for the systemsettings package.
Group: Documentation

%description doc
doc components for the systemsettings package.


%package lib
Summary: lib components for the systemsettings package.
Group: Libraries
Requires: systemsettings-data = %{version}-%{release}
Requires: systemsettings-license = %{version}-%{release}

%description lib
lib components for the systemsettings package.


%package license
Summary: license components for the systemsettings package.
Group: Default

%description license
license components for the systemsettings package.


%package locales
Summary: locales components for the systemsettings package.
Group: Default

%description locales
locales components for the systemsettings package.


%prep
%setup -q -n systemsettings-5.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539124399
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1539124399
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/systemsettings
cp COPYING %{buildroot}/usr/share/doc/systemsettings/COPYING
cp COPYING.DOC %{buildroot}/usr/share/doc/systemsettings/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang systemsettings

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/systemsettings5

%files data
%defattr(-,root,root,-)
/usr/share/applications/kdesystemsettings.desktop
/usr/share/applications/systemsettings.desktop
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/ActionMenu.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/CategoriesPage.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/IntroIcon.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/SubCategoryPage.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/introPage.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/main.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/metadata.desktop
/usr/share/kservices5/settings-appearance-applicationstyle.desktop
/usr/share/kservices5/settings-appearance-color.desktop
/usr/share/kservices5/settings-appearance-font.desktop
/usr/share/kservices5/settings-appearance-icons.desktop
/usr/share/kservices5/settings-appearance-workspacetheme.desktop
/usr/share/kservices5/settings-appearance.desktop
/usr/share/kservices5/settings-classic-view.desktop
/usr/share/kservices5/settings-hardware-display.desktop
/usr/share/kservices5/settings-hardware-input.desktop
/usr/share/kservices5/settings-hardware-multimedia.desktop
/usr/share/kservices5/settings-hardware-peripherals.desktop
/usr/share/kservices5/settings-hardware-powermanagement.desktop
/usr/share/kservices5/settings-hardware-removable-storage.desktop
/usr/share/kservices5/settings-hardware.desktop
/usr/share/kservices5/settings-icon-view.desktop
/usr/share/kservices5/settings-network-bluetooth.desktop
/usr/share/kservices5/settings-network-connectivity.desktop
/usr/share/kservices5/settings-network-networksettings.desktop
/usr/share/kservices5/settings-network.desktop
/usr/share/kservices5/settings-personalization-accessibility.desktop
/usr/share/kservices5/settings-personalization-accountdetails.desktop
/usr/share/kservices5/settings-personalization-applications.desktop
/usr/share/kservices5/settings-personalization-notification.desktop
/usr/share/kservices5/settings-personalization-regionalsettings.desktop
/usr/share/kservices5/settings-personalization.desktop
/usr/share/kservices5/settings-sidebar-view.desktop
/usr/share/kservices5/settings-workspace-desktopbehavior.desktop
/usr/share/kservices5/settings-workspace-search.desktop
/usr/share/kservices5/settings-workspace-session.desktop
/usr/share/kservices5/settings-workspace-shortcuts.desktop
/usr/share/kservices5/settings-workspace-windowmanagement.desktop
/usr/share/kservices5/settings-workspace.desktop
/usr/share/kservicetypes5/systemsettingscategory.desktop
/usr/share/kservicetypes5/systemsettingsexternalapp.desktop
/usr/share/kservicetypes5/systemsettingsview.desktop
/usr/share/kxmlgui5/systemsettings/systemsettingsui.rc
/usr/share/systemsettings/classic/main.html
/usr/share/systemsettings/classic/systemsettings-classic.css
/usr/share/systemsettings/systemsettings.kcfg
/usr/share/xdg/systemsettings.categories

%files dev
%defattr(-,root,root,-)
/usr/include/systemsettingsview/BaseData.h
/usr/include/systemsettingsview/BaseMode.h
/usr/include/systemsettingsview/MenuItem.h
/usr/include/systemsettingsview/MenuModel.h
/usr/include/systemsettingsview/MenuProxyModel.h
/usr/include/systemsettingsview/ModuleView.h
/usr/include/systemsettingsview/systemsettingsview_export.h
/usr/lib64/libsystemsettingsview.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/systemsettings/index.cache.bz2
/usr/share/doc/HTML/ca/systemsettings/index.docbook
/usr/share/doc/HTML/de/systemsettings/index.cache.bz2
/usr/share/doc/HTML/de/systemsettings/index.docbook
/usr/share/doc/HTML/en/systemsettings/index.cache.bz2
/usr/share/doc/HTML/en/systemsettings/index.docbook
/usr/share/doc/HTML/it/systemsettings/index.cache.bz2
/usr/share/doc/HTML/it/systemsettings/index.docbook
/usr/share/doc/HTML/nl/systemsettings/index.cache.bz2
/usr/share/doc/HTML/nl/systemsettings/index.docbook
/usr/share/doc/HTML/pt/systemsettings/index.cache.bz2
/usr/share/doc/HTML/pt/systemsettings/index.docbook
/usr/share/doc/HTML/pt_BR/systemsettings/index.cache.bz2
/usr/share/doc/HTML/pt_BR/systemsettings/index.docbook
/usr/share/doc/HTML/ru/systemsettings/index.cache.bz2
/usr/share/doc/HTML/ru/systemsettings/index.docbook
/usr/share/doc/HTML/sv/systemsettings/index.cache.bz2
/usr/share/doc/HTML/sv/systemsettings/index.docbook
/usr/share/doc/HTML/uk/systemsettings/index.cache.bz2
/usr/share/doc/HTML/uk/systemsettings/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsystemsettingsview.so.3
/usr/lib64/qt5/plugins/classic_mode.so
/usr/lib64/qt5/plugins/icon_mode.so
/usr/lib64/qt5/plugins/systemsettings_sidebar_mode.so

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/systemsettings/COPYING
/usr/share/doc/systemsettings/COPYING.DOC

%files locales -f systemsettings.lang
%defattr(-,root,root,-)

