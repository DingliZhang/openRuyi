# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Mahno <bestwow2014@gmail.com>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmodulemd
Version:        2.15.2
Release:        %autorelease
Summary:        Module metadata manipulation library
# COPYING:      MIT
## not in any binary package
# contrib/coverity-modeling.c:  GPL-2.0-or-later
# contrib/release-tools/semver: GPL-3.0-only
# modulemd/tests/test_data/f29.yaml:            Apache-2.0
# modulemd/tests/test_data/f29-updates.yaml:    Apache-2.0
# xml_specs/reduced/tests/good/module_stream_build_license.xml: MIT AND GPL-3.0-or-later
License:        MIT
SourceLicense:  %{license} AND GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/fedora-modularity/libmodulemd
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/modulemd-%{version}.tar.xz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/modulemd-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
#Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
BuildSystem:    meson
BuildOption(conf): -Drpmio=enabled
BuildOption(conf): -Dskip_introspection=false
BuildOption(conf): -Dtest_installed_lib=false
BuildOption(conf): -Dwith_docs=false
BuildOption(conf): -Dwith_manpages=enabled

#BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(gobject-2.0) pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(yaml-0.1)
# doc gen tool is disabled to make this pkg usable ASAP
#BuildRequires:  pkgconfig(gtk-doc)
#BuildRequires:  glib2-doc
BuildRequires:  rpm-devel
BuildRequires:  python3-devel python3-pygobject

%description
C library for manipulating module metadata files.
See https://github.com/fedora-modularity/libmodulemd/blob/main/README.md for
more details.

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-pygobject
Requires:       python3-six

%description -n python3-%{name}
Python3 bindings for %{name}.

%package devel
Summary:        Development files for libmodulemd
Requires:       libmodulemd

%description devel
Development files for %{name}.

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/modulemd-validator
%{_mandir}/man1/modulemd-validator.1*
%{_libdir}/libmodulemd.so.2*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Modulemd-2.0.typelib

%files devel
%{_libdir}/libmodulemd.so
%{_libdir}/pkgconfig/modulemd-2.0.pc
%{_includedir}/modulemd-2.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Modulemd-2.0.gir

%files -n python3-%{name}
%{python3_sitearch}/gi/overrides/

%changelog
%{?autochangelog}
