# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           purego
%define go_import_path  github.com/ebitengine/purego

Name:           go-github-ebitengine-purego
Version:        0.11.0
Release:        %autorelease
Summary:        Call C functions from Go without cgo
License:        Apache-2.0
URL:            https://github.com/ebitengine/purego
#!RemoteAsset:  sha256:7245f11bc20e48bf99d1267457eee7fedd1193090cabf98222ce62cc17b32278
Source0:        https://github.com/ebitengine/purego/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
PureGo loads shared libraries and calls C functions from Go without requiring
cgo at build time.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
