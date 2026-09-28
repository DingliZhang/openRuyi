# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctr
%global full_version 0.10.0-rc.3
%global pkgname ctr-0.10.0-rc.3

Name:           rust-ctr-0.10.0-rc.3
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "ctr"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/block-modes
#!RemoteAsset:  sha256:65ea71550d18331d179854662ab330bb54306b9b56020d0466aae2a58f4e17c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cipher-0.5.0-rc.8/default) >= 0.5.0-rc.8
Requires:       crate(cipher-0.5.0-rc.8/stream-wrapper) >= 0.5.0-rc.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ctr"

%package     -n %{name}+alloc
Summary:        CTR block modes of operation - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5.0-rc.8/alloc) >= 0.5.0-rc.8
Requires:       crate(cipher-0.5.0-rc.8/stream-wrapper) >= 0.5.0-rc.8
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ctr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block-padding
Summary:        CTR block modes of operation - feature "block-padding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5.0-rc.8/block-padding) >= 0.5.0-rc.8
Requires:       crate(cipher-0.5.0-rc.8/stream-wrapper) >= 0.5.0-rc.8
Provides:       crate(%{pkgname}/block-padding) = %{version}

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust ctr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        CTR block modes of operation - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5.0-rc.8/stream-wrapper) >= 0.5.0-rc.8
Requires:       crate(cipher-0.5.0-rc.8/zeroize) >= 0.5.0-rc.8
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ctr crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
