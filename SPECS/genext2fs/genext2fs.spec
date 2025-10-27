# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           genext2fs
Version:        1.5.0
Release:        %autorelease
Summary:        ext2 filesystem generator
License:        GPL-2.0-only
URL:            https://github.com/bestouff/genext2fs/
#!RemoteAsset
Source0:        https://github.com/bestouff/genext2fs/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf automake gcc make libtool

%description
genext2fs generates an ext2 filesystem as a normal (non-root) user.
It does not require you to mount the image file to copy files on it,
nor does it require that you become the superuser to make device nodes.

%conf -p
autoreconf -fi

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/genext2fs
%{_mandir}/man8/genext2fs.8*

%changelog
%{?autochangelog}
