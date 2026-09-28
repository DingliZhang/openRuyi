# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           crypto
%define go_import_path  golang.org/x/crypto

# We need to to avoid circular dependency between go-golang-x-crypto and go-golang-x-net
# So we need to manually download the right version of golang.org/x/net and place it in the source tree
# Check https://github.com/golang/crypto/blob/master/go.mod for the correct version
%define go_golang_x_net_version 0.47.0

Name:           go-golang-x-crypto
Version:        0.57.0
Release:        %autorelease
Summary:        Go supplementary cryptography libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/crypto
VCS:            git:https://github.com/golang/crypto
#!RemoteAsset:  sha256:a0508c7abb5e233f8dd123a7db3dfb828c143530c81a71395a8a5a8715f94335
Source0:        https://github.com/golang/crypto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# TestWithPebble starts an external Pebble ACME server integration environment,
# which is not available in OBS.
# - HNO3Miracle
Patch2001:      2001-skip-pebble-integration-test.patch

BuildOption(check):  -skip TestWithPebble

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(golang.org/x/crypto) = %{version}

Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
This package provides cryptographic algorithms and protocols.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
