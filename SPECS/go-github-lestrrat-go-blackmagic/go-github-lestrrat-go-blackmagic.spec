# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           blackmagic
%define go_import_path  github.com/lestrrat-go/blackmagic

Name:           go-github-lestrrat-go-blackmagic
Version:        1.0.4
Release:        %autorelease
Summary:        Reflection helpers for assigning typed optional values
License:        MIT
URL:            https://github.com/lestrrat-go/blackmagic
#!RemoteAsset:  sha256:42d4353dd4d4879ab5c3a4d42bc406d29f6c5c33b15b4ec20b287db94da21e0c
Source0:        https://github.com/lestrrat-go/blackmagic/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/lestrrat-go/blackmagic) = %{version}

%description
blackmagic contains small reflect-based helpers used by lestrrat-go
libraries to assign optional field values.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
