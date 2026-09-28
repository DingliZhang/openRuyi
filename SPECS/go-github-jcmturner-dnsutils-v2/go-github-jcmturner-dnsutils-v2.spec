# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dnsutils
# Install the repository root so both the legacy sources and the v2
# subtree retain their canonical import paths.
%define go_import_path  github.com/jcmturner/dnsutils

Name:           go-github-jcmturner-dnsutils-v2
Version:        2.0.0
Release:        %autorelease
Summary:        DNS utilities for Go Kerberos clients
License:        Apache-2.0
URL:            https://github.com/jcmturner/dnsutils
#!RemoteAsset:  sha256:cf159f3bad90db84dc8c8814d10f10560c7ec83c4ec160dfad9502d4a17c9958
Source0:        https://github.com/jcmturner/dnsutils/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/jcmturner/dnsutils/v2) = %{version}
Provides:       go(%{go_import_path}) = %{version}

%description
Dnsutils provides DNS discovery helpers used by Go Kerberos clients.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
