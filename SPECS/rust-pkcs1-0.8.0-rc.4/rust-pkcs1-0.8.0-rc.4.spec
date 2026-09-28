# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkcs1
%global full_version 0.8.0-rc.4
%global pkgname pkcs1-0.8.0-rc.4

Name:           rust-pkcs1-0.8.0-rc.4
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "pkcs1"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/pkcs1
#!RemoteAsset:  sha256:986d2e952779af96ea048f160fd9194e1751b4faea78bcf3ceb456efe008088e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.8.0-rc.9/default) >= 0.8.0-rc.9
Requires:       crate(der-0.8.0-rc.9/oid) >= 0.8.0-rc.9
Requires:       crate(spki-0.8.0-rc.4/default) >= 0.8.0-rc.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pkcs1"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Requires:       crate(der-0.8.0-rc.9/alloc) >= 0.8.0-rc.9
Requires:       crate(der-0.8.0-rc.9/oid) >= 0.8.0-rc.9
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.8.0-rc.9/oid) >= 0.8.0-rc.9
Requires:       crate(der-0.8.0-rc.9/pem) >= 0.8.0-rc.9
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.8.0-rc.9/oid) >= 0.8.0-rc.9
Requires:       crate(der-0.8.0-rc.9/std) >= 0.8.0-rc.9
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.8.0-rc.9/oid) >= 0.8.0-rc.9
Requires:       crate(der-0.8.0-rc.9/zeroize) >= 0.8.0-rc.9
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
