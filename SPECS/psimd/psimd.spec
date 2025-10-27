# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define commit 072586a71b55b7f8c584153d223e95687148a900
%define commitdate 20200517

Name:           psimd-devel
Version:        0.0.%{commitdate}
Release:        %autorelease
Summary:        P(ortable) SIMD intrinsics library (header-only)
License:        MIT
URL:            https://github.com/Maratyszcza/psimd
#!RemoteAsset
Source0:        https://github.com/Maratyszcza/psimd/archive/%{commit}/psimd-072586a.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5
BuildRequires:  cmake

%description
psimd is a header-only C/C++ library that provides a portable interface to
128-bit SIMD intrinsics on x86, ARM, and WebAssembly.

%files
%doc README.md
%license LICENSE
%{_includedir}/psimd.h

%changelog
%{?autochangelog}
