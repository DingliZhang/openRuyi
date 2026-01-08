# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Avoid: error: ‘_FORTIFY_SOURCE’ redefined
%global build_cflags $(echo "%{build_cflags}" | sed -e 's/-D_FORTIFY_SOURCE=3//')

%global commit b233050

Name:               fcoe-utils
Version:            1.0.34
Release:            %autorelease
Summary:            Fibre Channel over Ethernet utilities
License:            GPL-2.0-only
URL:                http://www.open-fcoe.org
#!RemoteAsset
Source:             https://github.com/openSUSE/fcoe-utils/archive/%{commit}.tar.gz
Patch0:             0001-fcoemon-add-snprintf-string-precision-modifiers-in-f.patch
Patch1:             0002-Don-t-attempt-to-memcpy-zero-bytes.patch
BuildSystem:        autotools

BuildOption(conf): --with-systemdsystemunitdir=%{_unitdir}

BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      libtool
BuildRequires:      pkgconfig(pciaccess)
BuildRequires:      pkgconfig(lldpad)
BuildRequires:      systemd-rpm-macros
BuildRequires:      make gcc
Requires:           lldpad
Requires:           iproute2
Requires:           device-mapper-multipath
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
Fibre Channel over Ethernet utilities: fcoeadm for configuration and
fcoemon service for DCB Ethernet QOS filter management.

%conf -p
./bootstrap.sh

%install -a
rm -rf %{buildroot}/etc/init.d
install -d %{buildroot}%{_libexecdir}/fcoe
for file in contrib/*.sh debug/*sh; do
    install -m 755 ${file} %{buildroot}%{_libexecdir}/fcoe/
done

%post
%systemd_post fcoe.service fcoemon.socket

%preun
%systemd_preun fcoe.service fcoemon.socket

%postun
%systemd_postun_with_restart fcoe.service fcoemon.socket

%files
%doc README COPYING QUICKSTART
%{_sbindir}/*
%{_mandir}/man8/*
%{_unitdir}/fcoe.service
%{_unitdir}/fcoemon.socket
%config(noreplace) %{_sysconfdir}/fcoe/cfg-ethx
%config(noreplace) %{_sysconfdir}/fcoe/config
%{_datadir}/bash-completion/completions/*
%{_libexecdir}/fcoe/

%changelog
%{?autochangelog}
