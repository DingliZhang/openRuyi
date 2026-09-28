# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name internal-russh-forked-ssh-key
%global full_version 0.6.18+upstream-0.6.7
%global pkgname internal-russh-forked-ssh-key-0.6

Name:           rust-internal-russh-forked-ssh-key-0.6
Version:        0.6.18
Release:        %autorelease
Summary:        Rust crate "internal-russh-forked-ssh-key"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Eugeny/RustCrypto-SSH/
#!RemoteAsset:  sha256:25f8a978272e3cbdf4768f7363eb1c8e1e6ba63c52a3ed05e29e222da4aec7cb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.7.0-rc.28/alloc) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/default) >= 0.7.0-rc.28
Requires:       crate(sha2-0.11.0-rc.5) >= 0.11.0-rc.5
Requires:       crate(signature-3.0.0-rc.10) >= 3.0.0-rc.10
Requires:       crate(ssh-cipher-0.2/default) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/base64) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/default) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/pem) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/sha2) >= 0.2.0
Requires:       crate(subtle-2) >= 2.5.0
Requires:       crate(zeroize-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/getrandom) = %{version}
Provides:       crate(%{pkgname}/hazmat-allow-insecure-rsa-keys) = %{version}

%description
Source code for takopackized Rust crate "internal-russh-forked-ssh-key"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-3.0.0-rc.10/alloc) >= 3.0.0-rc.10
Requires:       crate(ssh-encoding-0.2/alloc) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/base64) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/pem) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/sha2) >= 0.2.0
Requires:       crate(zeroize-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "crypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ed25519) = %{version}
Requires:       crate(%{pkgname}/p256) = %{version}
Requires:       crate(%{pkgname}/p384) = %{version}
Requires:       crate(%{pkgname}/p521) = %{version}
Requires:       crate(%{pkgname}/rsa) = %{version}
Provides:       crate(%{pkgname}/crypto) = %{version}

%description -n %{name}+crypto
This metapackage enables feature "crypto" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dsa
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "dsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(dsa-0.7.0-rc.13/hazmat) >= 0.7.0-rc.13
Requires:       crate(num-bigint-dig-0.8/std) >= 0.8.4
Requires:       crate(sha1-0.11.0-rc.5/oid) >= 0.11.0-rc.5
Requires:       crate(signature-3.0.0-rc.10/rand-core) >= 3.0.0-rc.10
Provides:       crate(%{pkgname}/dsa) = %{version}

%description -n %{name}+dsa
This metapackage enables feature "dsa" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "ecdsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16) >= 0.17.0-rc.16
Requires:       crate(sec1-0.8.0-rc.13/point) >= 0.8.0-rc.13
Provides:       crate(%{pkgname}/ecdsa) = %{version}

%description -n %{name}+ecdsa
This metapackage enables feature "ecdsa" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ed25519
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "ed25519"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(ed25519-dalek-3.0.0-pre.6) >= 3.0.0-pre.6
Provides:       crate(%{pkgname}/ed25519) = %{version}

%description -n %{name}+ed25519
This metapackage enables feature "ed25519" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encryption
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "encryption"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(bcrypt-pbkdf-0.10/alloc) >= 0.10.0
Requires:       crate(ssh-cipher-0.2/aes-cbc) >= 0.2.0
Requires:       crate(ssh-cipher-0.2/aes-ctr) >= 0.2.0
Requires:       crate(ssh-cipher-0.2/aes-gcm) >= 0.2.0
Requires:       crate(ssh-cipher-0.2/chacha20poly1305) >= 0.2.0
Provides:       crate(%{pkgname}/encryption) = %{version}

%description -n %{name}+encryption
This metapackage enables feature "encryption" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p256
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "p256"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(p256-0.14.0-rc.7/ecdsa) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/p256) = %{version}

%description -n %{name}+p256
This metapackage enables feature "p256" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p384
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "p384"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(p384-0.14.0-rc.7/ecdsa) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/p384) = %{version}

%description -n %{name}+p384
This metapackage enables feature "p384" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p521
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "p521"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(p521-0.14.0-rc.7/ecdsa) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/p521) = %{version}

%description -n %{name}+p521
This metapackage enables feature "p521" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ppk
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "ppk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(argon2-0.5/alloc) >= 0.5.0
Requires:       crate(hex-0.4/default) >= 0.4.0
Requires:       crate(hmac-0.13.0-rc.5/default) >= 0.13.0-rc.5
Requires:       crate(sha1-0.11.0-rc.5/oid) >= 0.11.0-rc.5
Requires:       crate(ssh-cipher-0.2/aes-cbc) >= 0.2.0
Provides:       crate(%{pkgname}/ppk) = %{version}

%description -n %{name}+ppk
This metapackage enables feature "ppk" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rsa
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(num-bigint-dig-0.8/std) >= 0.8.4
Requires:       crate(rsa-0.10.0-rc.16/sha2) >= 0.10.0-rc.16
Provides:       crate(%{pkgname}/rsa) = %{version}

%description -n %{name}+rsa
This metapackage enables feature "rsa" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rsa-sha1
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "rsa-sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rsa) = %{version}
Requires:       crate(sha1-0.11.0-rc.5/oid) >= 0.11.0-rc.5
Provides:       crate(%{pkgname}/rsa-sha1) = %{version}

%description -n %{name}+rsa-sha1
This metapackage enables feature "rsa-sha1" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.16
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(p256-0.14.0-rc.7/ecdsa) >= 0.14.0-rc.7
Requires:       crate(p256-0.14.0-rc.7/std) >= 0.14.0-rc.7
Requires:       crate(p384-0.14.0-rc.7/ecdsa) >= 0.14.0-rc.7
Requires:       crate(p384-0.14.0-rc.7/std) >= 0.14.0-rc.7
Requires:       crate(p521-0.14.0-rc.7/ecdsa) >= 0.14.0-rc.7
Requires:       crate(p521-0.14.0-rc.7/std) >= 0.14.0-rc.7
Requires:       crate(rsa-0.10.0-rc.16/sha2) >= 0.10.0-rc.16
Requires:       crate(rsa-0.10.0-rc.16/std) >= 0.10.0-rc.16
Requires:       crate(sec1-0.8.0-rc.13/point) >= 0.8.0-rc.13
Requires:       crate(sec1-0.8.0-rc.13/std) >= 0.8.0-rc.13
Requires:       crate(ssh-encoding-0.2/base64) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/pem) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/sha2) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tdes
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "tdes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encryption) = %{version}
Requires:       crate(ssh-cipher-0.2/tdes) >= 0.2.0
Provides:       crate(%{pkgname}/tdes) = %{version}

%description -n %{name}+tdes
This metapackage enables feature "tdes" for the Rust internal-russh-forked-ssh-key crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
