# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           msgp
%define go_import_path  github.com/tinylib/msgp
# TinyGo integration tests compile for embedded targets using a separate
# compiler and target runtimes that are not packaged in openRuyi.
%define go_test_exclude  %{go_import_path}/tinygotest

Name:           go-github-tinylib-msgp
Version:        1.6.4
Release:        %autorelease
Summary:        A Go code generator for MessagePack / msgpack.org
License:        MIT
URL:            https://github.com/tinylib/msgp
#!RemoteAsset:  sha256:1da18b32bb80d663c2a7343987acbde7396253c326f1dc9d52178512e658cb5a
Source0:        https://github.com/tinylib/msgp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/tinylib/msgp) = %{version}

Requires:       go(github.com/philhofer/fwd)
Requires:       go(golang.org/x/tools)

%description
Msgp is a code generation tool and serialization library for MessagePack.

%check -p
# Upstream's prepare target builds msgp before generating its unit and
# integration fixtures. Put the generator on PATH for go:generate directives.
%go_common
%go_prep
go build -o %{_builddir}/msgp-test-bin/msgp .
export PATH=%{_builddir}/msgp-test-bin:${PATH}
go generate ./msgp ./_generated

%check -a
# Go's ./... pattern omits underscore-prefixed directories; test the generated
# integration suite explicitly after the default package checks.
go test -v ./_generated

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
