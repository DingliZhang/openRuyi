# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sdk-go
%define go_import_path  github.com/ionos-cloud/sdk-go/v6
# Upstream ships several independent example main programs in one directory.
%global go_test_exclude_glob %{go_import_path}/examples*

Name:           go-github-ionos-cloud-sdk-go-v6
Version:        6.3.11
Release:        %autorelease
Summary:        Go SDK for the IONOS Cloud API
License:        Apache-2.0
URL:            https://github.com/ionos-cloud/sdk-go
#!RemoteAsset:  sha256:e09d19be78d9c5210aeaa9e7880135978a66bd290b390a76b39961fe3e09d173
Source0:        https://github.com/ionos-cloud/sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/oauth2)

Provides:       go(github.com/ionos-cloud/sdk-go/v6) = %{version}

Requires:       go(golang.org/x/oauth2)

%description
The IONOS Cloud SDK for Go provides client APIs for managing IONOS Cloud
resources through the Cloud API, including data centers, servers,
volumes, networks and related infrastructure resources.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
