# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lru
%define go_import_path  github.com/phuslu/lru

Name:           go-github-phuslu-lru
Version:        1.0.23
Release:        %autorelease
Summary:        High-performance generic LRU cache for Go
License:        MIT
URL:            https://github.com/phuslu/lru
#!RemoteAsset:  sha256:ff6efe8ff19251fe4b48ce4a063a0e94fc2b1c359f5d94145a5fd5709bae2501
Source0:        https://github.com/phuslu/lru/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides generic LRU and TTL caches optimized for low allocation
overhead and concurrent access.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
