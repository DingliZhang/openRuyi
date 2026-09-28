# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aes
%global full_version 0.9.0-rc.4
%global pkgname aes-0.9.0-rc.4

Name:           rust-aes-0.9.0-rc.4
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "aes"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-ciphers
#!RemoteAsset:  sha256:04097e08a47d9ad181c2e1f4a5fabc9ae06ce8839a333ba9a949bcb0d31fd2a3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.5.0-rc.8/default) >= 0.5.0-rc.8
Requires:       crate(cpubits-0.1.0-rc.3/default) >= 0.1.0-rc.3
Requires:       crate(cpufeatures-0.2/default) >= 0.2.12

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Rijndael)
Source code for takopackized Rust crate "aes"

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Advanced Encryption Standard (a.k.a - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/aarch64) >= 1.5.6
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
Rijndael)
This metapackage enables feature "zeroize" for the Rust aes crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
