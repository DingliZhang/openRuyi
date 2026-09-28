# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           enterprise-certificate-proxy
%define go_import_path  github.com/googleapis/enterprise-certificate-proxy
# Darwin and Windows packages import platform-specific subpackages excluded by
# Linux build tags. Linux pkcs11 tests require softhsm, and http_proxy contains
# routing assertions that fail under the OBS test environment. - HNO3Miracle
%define go_test_exclude %{shrink:
    github.com/googleapis/enterprise-certificate-proxy/darwin
    github.com/googleapis/enterprise-certificate-proxy/http_proxy
    github.com/googleapis/enterprise-certificate-proxy/internal/signer/darwin
    github.com/googleapis/enterprise-certificate-proxy/internal/signer/linux/pkcs11
    github.com/googleapis/enterprise-certificate-proxy/internal/signer/windows
    github.com/googleapis/enterprise-certificate-proxy/linux
    github.com/googleapis/enterprise-certificate-proxy/windows
}

Name:           go-github-googleapis-enterprise-certificate-proxy
Version:        0.3.22
Release:        %autorelease
Summary:        Enterprise certificate proxy library for Go
License:        Apache-2.0
URL:            https://github.com/googleapis/enterprise-certificate-proxy
#!RemoteAsset:  sha256:53341b8b9621aa9c2ae40e1d523102230577325541f530bbb3f32ab2e3be16e7
Source0:        https://github.com/googleapis/enterprise-certificate-proxy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-pkcs11)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/googleapis/enterprise-certificate-proxy) = %{version}

Requires:       go(github.com/google/go-pkcs11)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
This package provides Go helpers for enterprise certificate based authentication.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
