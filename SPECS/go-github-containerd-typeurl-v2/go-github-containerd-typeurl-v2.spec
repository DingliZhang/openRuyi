# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           typeurl
%define go_import_path  github.com/containerd/typeurl/v2

Name:           go-github-containerd-typeurl-v2
Version:        2.3.0
Release:        %autorelease
Summary:        Go package for managing marshaled types to protobuf.Any
License:        Apache-2.0
URL:            https://github.com/containerd/typeurl
#!RemoteAsset:  sha256:a216d2d25150c5d1384c00dde25026f3a00546297afb4dacdaa0764e46991f01
Source0:        https://github.com/containerd/typeurl/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(google.golang.org/protobuf)

%description
A Go package for managing the registration, marshaling, and unmarshaling
of encoded types.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
