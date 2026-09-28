# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hjson-go
%define go_import_path  github.com/hjson/hjson-go/v4

Name:           go-github-hjson-hjson-go-v4
Version:        4.7.1
Release:        %autorelease
Summary:        Hjson implementation for Go
License:        MIT
URL:            https://github.com/hjson/hjson-go
#!RemoteAsset:  sha256:2881c114bcd194860155885e3c3586b6e41832818ea5cbf9c661a6a7990a79b6
Source0:        https://github.com/hjson/hjson-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package implements the Hjson human-friendly configuration format in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
