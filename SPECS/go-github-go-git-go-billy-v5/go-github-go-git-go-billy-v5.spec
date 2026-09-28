# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-billy
%define go_import_path  github.com/go-git/go-billy/v5

Name:           go-github-go-git-go-billy-v5
Version:        5.9.1
Release:        %autorelease
Summary:        Filesystem abstraction library for Go
License:        Apache-2.0
URL:            https://github.com/go-git/go-billy
#!RemoteAsset:  sha256:be22e89fd5e050782201778267080c9b92b89e04e2cef5299d41aee84359a6a6
Source0:        https://github.com/go-git/go-billy/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/go-git/go-billy/v5) = %{version}

Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/kr/text)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/check.v1)

%description
go-billy provides filesystem interfaces and implementations used by go-git,
including OS-backed, in-memory, and helper filesystem backends.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
