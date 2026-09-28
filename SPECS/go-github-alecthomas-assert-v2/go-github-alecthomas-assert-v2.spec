# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/alecthomas/assert/v2

Name:           go-github-alecthomas-assert-v2
Version:        2.11.0
Release:        %autorelease
Summary:        Generic assertion library for Go tests
License:        MIT
URL:            https://github.com/alecthomas/assert
#!RemoteAsset:  sha256:56f776f1d5e1888ef35b4c01ae96dd7d47f706911288a774b5bc199dcec734da
Source0:        https://github.com/alecthomas/assert/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/repr)
BuildRequires:  go(github.com/hexops/gotextdiff)

Provides:       go(github.com/alecthomas/assert/v2) = %{version}

Requires:       go(github.com/alecthomas/repr)
Requires:       go(github.com/hexops/gotextdiff)

%description
assert provides concise generic assertion helpers and readable value diffs for
Go unit tests.

%files
%doc README*
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
