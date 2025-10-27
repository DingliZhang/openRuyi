# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:               console-setup
Version:            1.242
Release:            %autorelease
Summary:            Tools for configuring the console font and keyboard
License:            GPL-2.0-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
URL:                https://packages.debian.org/sid/console-setup
#!RemoteAsset
Source:             https://ftp.debian.org/debian/pool/main/c/console-setup/console-setup_%{version}.tar.xz
BuildSystem:        autotools
Patch:              0001-fix-makefile.patch

BuildOption(install): prefix=%{_prefix}
BuildOption(install): exec_prefix=%{_exec_prefix}
BuildOption(install): bindir=%{_bindir}
BuildOption(install): sbindir=%{_sbindir}
BuildOption(install): sysconfdir=%{_sysconfdir}
BuildOption(install): datarootdir=%{_datadir}
BuildOption(install): mandir=%{_mandir}

BuildRequires:      perl
BuildRequires:      make
Requires:       kbd

%description
This package provides tools to configure the console's font and keyboard layout,
often using settings derived from the X Window System.

%package -n     bdf2psf
Summary:    Generate console fonts from BDF source fonts

%description -n bdf2psf
This package provides a command-line converter to build console fonts from BDF
sources.

# No configure
%conf

# No tests
%check

%files
%doc README COPYRIGHT CHANGES copyright.fonts copyright.xkb Fonts/copyright
%{_bindir}/ckbcomp
%{_bindir}/setupcon
%config(noreplace) %{_sysconfdir}/default/console-setup
%config(noreplace) %{_sysconfdir}/default/keyboard
%{_datadir}/consolefonts/
%{_datadir}/consoletrans/
%{_mandir}/man1/ckbcomp.1*
%{_mandir}/man1/setupcon.1*
%{_mandir}/man5/console-setup.5*
%{_mandir}/man5/keyboard.5*

%files -n bdf2psf
%license GPL-2
%{_bindir}/bdf2psf
%{_mandir}/man1/bdf2psf.1*
%{_datadir}/bdf2psf/

%changelog
%{?autochangelog}
