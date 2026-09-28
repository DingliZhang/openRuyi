# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name russh
%global full_version 0.60.3
%global pkgname russh-0.60

Name:           rust-russh-0.60
Version:        0.60.3
Release:        %autorelease
Summary:        Rust crate "russh"
License:        Apache-2.0
URL:            https://github.com/warp-tech/russh
#!RemoteAsset:  sha256:324b92f459d3e42da294e14e8eb150d2215fcfb7c966838bc1127cd68bc05a0d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aead-0.6.0-rc.10/default) >= 0.6.0-rc.10
Requires:       crate(aes-0.8/default) >= 0.8.0
Requires:       crate(aes-0.9/default) >= 0.9.0
Requires:       crate(aes-gcm-0.11.0-rc.3/default) >= 0.11.0-rc.3
Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(block-padding-0.3/default) >= 0.3.0
Requires:       crate(block-padding-0.3/std) >= 0.3.0
Requires:       crate(byteorder-1/default) >= 1.4.0
Requires:       crate(bytes-1/default) >= 1.7.0
Requires:       crate(cbc-0.1/default) >= 0.1.0
Requires:       crate(cbc-0.2/default) >= 0.2.0
Requires:       crate(cipher-0.5/default) >= 0.5.1
Requires:       crate(crypto-bigint-0.7.0-rc.28/alloc) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/default) >= 0.7.0-rc.28
Requires:       crate(ctr-0.10/default) >= 0.10.0
Requires:       crate(ctr-0.9/default) >= 0.9.0
Requires:       crate(curve25519-dalek-5.0.0-pre.6/default) >= 5.0.0-pre.6
Requires:       crate(data-encoding-2/default) >= 2.3.0
Requires:       crate(delegate-0.13/default) >= 0.13.0
Requires:       crate(der-0.8/default) >= 0.8.0
Requires:       crate(digest-0.10/default) >= 0.10.0
Requires:       crate(ecdsa-0.17.0-rc.16/default) >= 0.17.0-rc.16
Requires:       crate(ed25519-dalek-3.0.0-pre.6/alloc) >= 3.0.0-pre.6
Requires:       crate(ed25519-dalek-3.0.0-pre.6/default) >= 3.0.0-pre.6
Requires:       crate(ed25519-dalek-3.0.0-pre.6/pkcs8) >= 3.0.0-pre.6
Requires:       crate(ed25519-dalek-3.0.0-pre.6/rand-core) >= 3.0.0-pre.6
Requires:       crate(elliptic-curve-0.14.0-rc.28/default) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/ecdh) >= 0.14.0-rc.28
Requires:       crate(enum-dispatch-0.3/default) >= 0.3.13
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(generic-array-1/compat-0-14) >= 1.3.3
Requires:       crate(generic-array-1/default) >= 1.3.3
Requires:       crate(getrandom-0.2/default) >= 0.2.15
Requires:       crate(getrandom-0.2/js) >= 0.2.15
Requires:       crate(ghash-0.6/default) >= 0.6.0
Requires:       crate(hex-literal-1/default) >= 1.0.0
Requires:       crate(hkdf-0.13/default) >= 0.13.0
Requires:       crate(hmac-0.12/default) >= 0.12.0
Requires:       crate(hmac-0.13/default) >= 0.13.0
Requires:       crate(inout-0.1/default) >= 0.1.0
Requires:       crate(inout-0.1/std) >= 0.1.0
Requires:       crate(internal-russh-forked-ssh-key-0.6/default) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/ed25519) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/encryption) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/hazmat-allow-insecure-rsa-keys) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p256) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p384) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p521) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/ppk) >= 0.6.18
Requires:       crate(internal-russh-num-bigint-0.5/default) >= 0.5.0
Requires:       crate(internal-russh-num-bigint-0.5/rand-0-10) >= 0.5.0
Requires:       crate(keccak-0.2/default) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.11
Requires:       crate(md5-0.7/default) >= 0.7.0
Requires:       crate(ml-kem-0.3.0-rc.1/default) >= 0.3.0-rc.1
Requires:       crate(module-lattice-0.2/default) >= 0.2.0
Requires:       crate(num-bigint-0.4/default) >= 0.4.6
Requires:       crate(p256-0.14.0-rc.7/default) >= 0.14.0-rc.7
Requires:       crate(p256-0.14.0-rc.7/ecdh) >= 0.14.0-rc.7
Requires:       crate(p384-0.14.0-rc.7/default) >= 0.14.0-rc.7
Requires:       crate(p384-0.14.0-rc.7/ecdh) >= 0.14.0-rc.7
Requires:       crate(p521-0.14.0-rc.7/default) >= 0.14.0-rc.7
Requires:       crate(p521-0.14.0-rc.7/ecdh) >= 0.14.0-rc.7
Requires:       crate(pageant-0.2/default) >= 0.2.0
Requires:       crate(pbkdf2-0.12/default) >= 0.12.0
Requires:       crate(pbkdf2-0.13/default) >= 0.13.0
Requires:       crate(pkcs5-0.8.0-rc.13/default) >= 0.8.0-rc.13
Requires:       crate(pkcs8-0.11.0-rc.11/default) >= 0.11.0-rc.11
Requires:       crate(pkcs8-0.11.0-rc.11/encryption) >= 0.11.0-rc.11
Requires:       crate(pkcs8-0.11.0-rc.11/std) >= 0.11.0-rc.11
Requires:       crate(polyval-0.7/default) >= 0.7.1
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(rand-0.10/thread-rng) >= 0.10.0
Requires:       crate(rand-core-0.10/default) >= 0.10.0
Requires:       crate(russh-cryptovec-0.60/default) >= 0.60.3
Requires:       crate(russh-cryptovec-0.60/ssh-encoding) >= 0.60.3
Requires:       crate(russh-util-0.52/default) >= 0.52.0
Requires:       crate(salsa20-0.11/default) >= 0.11.0
Requires:       crate(scrypt-0.12/default) >= 0.12.0
Requires:       crate(sec1-0.8/default) >= 0.8.0
Requires:       crate(sec1-0.8/der) >= 0.8.0
Requires:       crate(sha1-0.10/default) >= 0.10.5
Requires:       crate(sha1-0.10/oid) >= 0.10.5
Requires:       crate(sha1-0.11/default) >= 0.11.0
Requires:       crate(sha2-0.10/default) >= 0.10.6
Requires:       crate(sha2-0.10/oid) >= 0.10.6
Requires:       crate(sha2-0.11/default) >= 0.11.0
Requires:       crate(sha3-0.11/default) >= 0.11.0
Requires:       crate(signature-3.0.0-rc.10/default) >= 3.0.0-rc.10
Requires:       crate(spki-0.8.0-rc.4/default) >= 0.8.0-rc.4
Requires:       crate(ssh-encoding-0.2/bytes) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/default) >= 0.2.0
Requires:       crate(subtle-2/default) >= 2.4.0
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tokio-1/default) >= 1.17.0
Requires:       crate(tokio-1/io-util) >= 1.17.0
Requires:       crate(tokio-1/net) >= 1.17.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.17.0
Requires:       crate(tokio-1/sync) >= 1.17.0
Requires:       crate(tokio-1/time) >= 1.17.0
Requires:       crate(typenum-1/default) >= 1.17.0
Requires:       crate(universal-hash-0.6/default) >= 0.6.1
Requires:       crate(zeroize-1/default) >= 1.7.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "russh"

%package     -n %{name}+bench
Summary:        Client and server SSH library - feature "_bench"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(criterion-0.7/default) >= 0.7.0
Requires:       crate(criterion-0.7/html-reports) >= 0.7.0
Provides:       crate(%{pkgname}/bench) = %{version}

%description -n %{name}+bench
This metapackage enables feature "_bench" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-trait
Summary:        Client and server SSH library - feature "async-trait"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.50
Provides:       crate(%{pkgname}/async-trait) = %{version}

%description -n %{name}+async-trait
This metapackage enables feature "async-trait" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+aws-lc-rs
Summary:        Client and server SSH library - feature "aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-rs-1/default) >= 1.16.2
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Client and server SSH library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(%{pkgname}/flate2) = %{version}
Requires:       crate(%{pkgname}/rsa) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+des
Summary:        Client and server SSH library - feature "des"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(des-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/des) = %{version}

%description -n %{name}+des
This metapackage enables feature "des" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dsa
Summary:        Client and server SSH library - feature "dsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(internal-russh-forked-ssh-key-0.6/dsa) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/ed25519) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/encryption) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/hazmat-allow-insecure-rsa-keys) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p256) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p384) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p521) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/ppk) >= 0.6.18
Provides:       crate(%{pkgname}/dsa) = %{version}

%description -n %{name}+dsa
This metapackage enables feature "dsa" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Client and server SSH library - feature "flate2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.15
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Client and server SSH library - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.14
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rsa
Summary:        Client and server SSH library - feature "rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(internal-russh-forked-ssh-key-0.6/ed25519) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/encryption) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/hazmat-allow-insecure-rsa-keys) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p256) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p384) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p521) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/ppk) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/rsa) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/rsa-sha1) >= 0.6.18
Requires:       crate(pkcs1-0.8.0-rc.4/default) >= 0.8.0-rc.4
Requires:       crate(rsa-0.10.0-rc.16/default) >= 0.10.0-rc.16
Provides:       crate(%{pkgname}/rsa) = %{version}

%description -n %{name}+rsa
This metapackage enables feature "rsa" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Client and server SSH library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(internal-russh-forked-ssh-key-0.6/ed25519) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/encryption) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/hazmat-allow-insecure-rsa-keys) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p256) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p384) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/p521) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/ppk) >= 0.6.18
Requires:       crate(internal-russh-forked-ssh-key-0.6/serde) >= 0.6.18
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yasna
Summary:        Client and server SSH library - feature "yasna" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(yasna-0.5/bit-vec) >= 0.5.0
Requires:       crate(yasna-0.5/default) >= 0.5.0
Requires:       crate(yasna-0.5/num-bigint) >= 0.5.0
Provides:       crate(%{pkgname}/legacy-ed25519-pkcs8-parser) = %{version}
Provides:       crate(%{pkgname}/yasna) = %{version}

%description -n %{name}+yasna
This metapackage enables feature "yasna" for the Rust russh crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "legacy-ed25519-pkcs8-parser" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
