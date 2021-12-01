#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : systemsettings
Version  : 5.23.4
Release  : 58
URL      : https://download.kde.org/stable/plasma/5.23.4/systemsettings-5.23.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.4/systemsettings-5.23.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: systemsettings-bin = %{version}-%{release}
Requires: systemsettings-data = %{version}-%{release}
Requires: systemsettings-lib = %{version}-%{release}
Requires: systemsettings-license = %{version}-%{release}
Requires: systemsettings-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kactivities-dev
BuildRequires : kactivities-stats-dev
BuildRequires : kcmutils-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kirigami2-dev
BuildRequires : kjs-dev
BuildRequires : krunner-dev
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
%setup -q -n systemsettings-5.23.4
cd %{_builddir}/systemsettings-5.23.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638364319
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1638364319
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/systemsettings
cp %{_builddir}/systemsettings-5.23.4/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/systemsettings/ea97eb88ae53ec41e26f8542176ab986d7bc943a
cp %{_builddir}/systemsettings-5.23.4/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/systemsettings/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/systemsettings-5.23.4/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/systemsettings/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/systemsettings-5.23.4/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/systemsettings/2123756e0b1fc8243547235a33c0fcabfe3b9a51
cp %{_builddir}/systemsettings-5.23.4/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/systemsettings/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/systemsettings-5.23.4/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/systemsettings/fa05e58320cb7c64786b26396f4b992579a628bc
cp %{_builddir}/systemsettings-5.23.4/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/systemsettings/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/systemsettings-5.23.4/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/systemsettings/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/systemsettings-5.23.4/runner/systemsettingsrunner.json.license %{buildroot}/usr/share/package-licenses/systemsettings/fd32940f125ecf08f9ad3cb0b64251688e927a90
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
/usr/share/kglobalaccel/systemsettings.desktop
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/images/plasma-logo.svg
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/CategoriesPage.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/CategoryItem.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/IntroIcon.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/SubCategoryPage.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/introPage.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/contents/ui/main.qml
/usr/share/kpackage/genericqml/org.kde.systemsettings.sidebar/metadata.desktop
/usr/share/kservicetypes5/systemsettingscategory.desktop
/usr/share/kservicetypes5/systemsettingsexternalapp.desktop
/usr/share/kservicetypes5/systemsettingsview.desktop
/usr/share/kxmlgui5/systemsettings/systemsettingsui.rc
/usr/share/metainfo/org.kde.systemsettings.metainfo.xml
/usr/share/qlogging-categories5/systemsettings.categories
/usr/share/systemsettings/categories/settings-appearance-color.desktop
/usr/share/systemsettings/categories/settings-appearance-font.desktop
/usr/share/systemsettings/categories/settings-appearance-icons.desktop
/usr/share/systemsettings/categories/settings-appearance.desktop
/usr/share/systemsettings/categories/settings-hardware-display.desktop
/usr/share/systemsettings/categories/settings-hardware-input.desktop
/usr/share/systemsettings/categories/settings-hardware-multimedia.desktop
/usr/share/systemsettings/categories/settings-hardware-peripherals.desktop
/usr/share/systemsettings/categories/settings-hardware-powermanagement.desktop
/usr/share/systemsettings/categories/settings-hardware-removable-storage.desktop
/usr/share/systemsettings/categories/settings-hardware.desktop
/usr/share/systemsettings/categories/settings-network-bluetooth.desktop
/usr/share/systemsettings/categories/settings-network-connectivity.desktop
/usr/share/systemsettings/categories/settings-network-networksettings.desktop
/usr/share/systemsettings/categories/settings-network.desktop
/usr/share/systemsettings/categories/settings-personalization-accessibility.desktop
/usr/share/systemsettings/categories/settings-personalization-accountdetails.desktop
/usr/share/systemsettings/categories/settings-personalization-applications.desktop
/usr/share/systemsettings/categories/settings-personalization-notification.desktop
/usr/share/systemsettings/categories/settings-personalization-regionalsettings.desktop
/usr/share/systemsettings/categories/settings-personalization.desktop
/usr/share/systemsettings/categories/settings-root-category.desktop
/usr/share/systemsettings/categories/settings-system-administration.desktop
/usr/share/systemsettings/categories/settings-workspace-desktopbehavior.desktop
/usr/share/systemsettings/categories/settings-workspace-search.desktop
/usr/share/systemsettings/categories/settings-workspace-session.desktop
/usr/share/systemsettings/categories/settings-workspace-shortcuts.desktop
/usr/share/systemsettings/categories/settings-workspace-windowmanagement.desktop
/usr/share/systemsettings/categories/settings-workspace.desktop
/usr/share/systemsettings/systemsettings.kcfg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/systemsettings/index.cache.bz2
/usr/share/doc/HTML/ca/systemsettings/index.docbook
/usr/share/doc/HTML/de/systemsettings/index.cache.bz2
/usr/share/doc/HTML/de/systemsettings/index.docbook
/usr/share/doc/HTML/en/systemsettings/index.cache.bz2
/usr/share/doc/HTML/en/systemsettings/index.docbook
/usr/share/doc/HTML/es/systemsettings/index.cache.bz2
/usr/share/doc/HTML/es/systemsettings/index.docbook
/usr/share/doc/HTML/id/systemsettings/index.cache.bz2
/usr/share/doc/HTML/id/systemsettings/index.docbook
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
/usr/lib64/qt5/plugins/kf5/krunner/krunner_systemsettings.so
/usr/lib64/qt5/plugins/systemsettingsview/icon_mode.so
/usr/lib64/qt5/plugins/systemsettingsview/systemsettings_sidebar_mode.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/systemsettings/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/systemsettings/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/systemsettings/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/systemsettings/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/systemsettings/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/systemsettings/fa05e58320cb7c64786b26396f4b992579a628bc
/usr/share/package-licenses/systemsettings/fd32940f125ecf08f9ad3cb0b64251688e927a90

%files locales -f systemsettings.lang
%defattr(-,root,root,-)

