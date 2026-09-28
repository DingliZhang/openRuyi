# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxkbfile
Version:        1.2.0
Release:        %autorelease
Summary:        X.Org X11 libxkbfile runtime library
License:        MIT-open-group AND HPND AND SMLNJ
URL:            https://gitlab.freedesktop.org/xorg/lib/libxkbfile/
#!RemoteAsset:  sha256:7f71884e5faf56fb0e823f3848599cf9b5a9afce51c90982baeb64f635233ebf
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libxkbfile-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)

%description
The libxkbfile library provides an interface to read and manipulate XKB
keymap files.

%package        devel
Summary:        X.Org X11 libxkbfile development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libxkbfile.

%files
%doc COPYING README.md
%{_libdir}/libxkbfile.so.1*

%files devel
%{_includedir}/X11/extensions/XKB*.h
%{_includedir}/X11/extensions/XKM*.h
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc

%changelog
%autochangelog
