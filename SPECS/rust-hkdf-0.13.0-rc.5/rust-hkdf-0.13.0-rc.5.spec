# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hkdf
%global full_version 0.13.0-rc.5
%global pkgname hkdf-0.13.0-rc.5

Name:           rust-hkdf-0.13.0-rc.5
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "hkdf"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/KDFs/
#!RemoteAsset:  sha256:cbb55385998ae66b8d2d5143c05c94b9025ab863966f0c94ce7a5fde30105092
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hmac-0.13.0-rc.5/default) >= 0.13.0-rc.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hkdf"

%package     -n %{name}+kdf
Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF) - feature "kdf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kdf-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/kdf) = %{version}

%description -n %{name}+kdf
This metapackage enables feature "kdf" for the Rust hkdf crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
