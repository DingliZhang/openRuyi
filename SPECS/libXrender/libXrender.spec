# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXrender
Version:        0.9.12
Release:        %autorelease
Summary:        X.Org X11 libXrender runtime library
License:        MIT
URL:            https://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxrender.git
#!RemoteAsset:  sha256:b832128da48b39c8d608224481743403ad1691bf4e554e4be9c174df171d1b97
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
X.Org X11 libXrender runtime library

%package        devel
Summary:        X.Org X11 libXrender development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
X.Org X11 libXrender development package

%conf -p
autoreconf -fiv

%files
%doc AUTHORS
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/xrender.pc
%{_docdir}/libXrender/*

%changelog
%autochangelog
