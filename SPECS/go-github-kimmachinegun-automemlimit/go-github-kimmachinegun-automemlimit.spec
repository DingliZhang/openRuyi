# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           automemlimit
%define go_import_path  github.com/KimMachineGun/automemlimit
# OBS builders do not expose a normal process cgroup layout;
# TestSetGoMemLimit observes "process is not in cgroup"
# instead of upstream's expected "cgroups is not supported on this system".
# Nested Go modules have their own module path/dependencies;
# skip them in %check so the parent package does not
# try to test unrelated internal tools. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/memlimit
    %{go_import_path}/examples/dynamic*
    %{go_import_path}/examples/logger*
    %{go_import_path}/examples/system*
}

Name:           go-github-kimmachinegun-automemlimit
Version:        1.0.0
Release:        %autorelease
Summary:        Automatically set GOMEMLIMIT from Linux cgroups memory limits
License:        MIT
URL:            https://github.com/KimMachineGun/automemlimit
#!RemoteAsset:  sha256:e6e06bc4a963bbceaa292665ea90c690984132bb20551e65c1b5d93977258252
Source0:        https://github.com/KimMachineGun/automemlimit/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pbnjay/memory)

Provides:       go(github.com/KimMachineGun/automemlimit) = %{version}

Requires:       go(github.com/pbnjay/memory)

%description
automemlimit sets a Go runtime memory limit based on cgroup or system memory.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/examples/dynamic
%exclude %{go_sys_gopath}/%{go_import_path}/examples/logger
%exclude %{go_sys_gopath}/%{go_import_path}/examples/system

%changelog
%autochangelog
