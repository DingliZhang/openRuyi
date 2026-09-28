# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-metrics
%define go_import_path  github.com/docker/go-metrics

Name:           go-github-docker-go-metrics
Version:        0.1.0
Release:        %autorelease
Summary:        Package for metrics collection in Docker projects
License:        Apache-2.0
URL:            https://github.com/docker/go-metrics
#!RemoteAsset:  sha256:2185b2383e84bec9a892cf5c1f4fb74ffbf8ccaa85c63045883e94da9b4ee30a
Source0:        https://github.com/docker/go-metrics/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/prometheus/client_golang)

Provides:       go(github.com/docker/go-metrics) = %{version}

Requires:       go(github.com/prometheus/client_golang)

%description
go-metrics is a Prometheus-based metrics collection helper library used across Docker/Moby projects.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
