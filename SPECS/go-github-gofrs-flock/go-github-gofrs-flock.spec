# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           flock
%define go_import_path  github.com/gofrs/flock

Name:           go-github-gofrs-flock
Version:        0.13.1
Release:        %autorelease
Summary:        Thread-safe file locking library for Go
License:        BSD-3-Clause
URL:            https://github.com/gofrs/flock
#!RemoteAsset:  sha256:b513db6e7cbebe001a24cddc2e063d21409f15b55d28915f7c626c708f9f792e
Source0:        https://github.com/gofrs/flock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sys)

%description
Flock implements thread-safe blocking and non-blocking file locks for Go
applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
