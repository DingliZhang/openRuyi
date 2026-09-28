# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           secp256k1
%define go_import_path  github.com/decred/dcrd/dcrec/secp256k1/v4
%define upstream_tag    dcrec/secp256k1/v%{version}

Name:           go-github-decred-dcrd-dcrec-secp256k1-v4
Version:        4.4.1
Release:        %autorelease
Summary:        secp256k1 elliptic curve operations for Go
License:        ISC
URL:            https://github.com/decred/dcrd
#!RemoteAsset:  sha256:5e30712b49e4c9460c4e0647d7b3e7aa5e88854b83b59d2432cd6e9948008253
Source0:        https://github.com/decred/dcrd/archive/refs/tags/%{upstream_tag}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/decred/dcrd/crypto/blake256)

Provides:       go(github.com/decred/dcrd/dcrec/secp256k1/v4) = %{version}

Requires:       go(github.com/decred/dcrd/crypto/blake256)

%description
secp256k1/v4 is the nested dcrd module that implements secp256k1 field,
scalar, and ECDSA operations. It is required by lestrrat-go/jwx/v2.

%prep -a
# Nested module github.com/decred/dcrd/dcrec/secp256k1/v4.
# go2spec cannot pack dcrd nested module tags (version field is mangled).
find . -maxdepth 1 -mindepth 1 -not -name dcrec -not -name LICENSE -not -name '_build' -exec rm -rf {} +
find ./dcrec -mindepth 1 -maxdepth 1 -not -name secp256k1 -exec rm -rf {} +
shopt -s dotglob && mv dcrec/secp256k1/* . && rmdir dcrec/secp256k1 dcrec

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
