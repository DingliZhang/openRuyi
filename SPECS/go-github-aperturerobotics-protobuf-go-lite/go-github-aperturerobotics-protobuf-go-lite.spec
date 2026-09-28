# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protobuf-go-lite
%define go_import_path  github.com/aperturerobotics/protobuf-go-lite
# Generator integration tests invoke protoc and Go module commands, which are
# incompatible with the GOPATH mode required by the golangmodules build system.
# A cmd tool, -- Jvle
%define go_test_exclude  github.com/aperturerobotics/protobuf-go-lite/cmd/protoc-gen-go-lite

Name:           go-github-aperturerobotics-protobuf-go-lite
Version:        0.18.0
Release:        %autorelease
Summary:        Reflection-free Protobuf for Go.
License:        BSD-3-Clause
URL:            https://github.com/aperturerobotics/protobuf-go-lite
#!RemoteAsset:  sha256:f4baf8ecbfe5531aeff211f2561c1c6dd7dbd2f5f35e491bf96b45a9f798d839
Source0:        https://github.com/aperturerobotics/protobuf-go-lite/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aperturerobotics/json-iterator-lite)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/aperturerobotics/protobuf-go-lite) = %{version}

Requires:       go(github.com/aperturerobotics/json-iterator-lite)
Requires:       go(google.golang.org/protobuf)

%description
protobuf-go-lite is a stripped-down version of the protobuf-go code
generator modified to work without reflection and merged with vtprotobuf
to provide modular features with static code generation for
marshal/unmarshal, size, clone, equal, text, and JSON. JSON support is
derived from a fork of protoc-gen-go-json.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
