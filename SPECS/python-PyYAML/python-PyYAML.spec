# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-PyYAML
Version:        6.0.2
Release:        %autorelease
Summary:        YAML parser and emitter for Python
License:        MIT
URL:            https://github.com/yaml/pyyaml
#!RemoteAsset
Source:         https://github.com/yaml/pyyaml/archive/%{version}.tar.gz

BuildRequires:  libyaml-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  expat

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistence.

%package     -n python3-PyYAML
Summary:        YAML parser and emitter for Python
%py_provides    python3-yaml
# For lazy people - 251
%py_provides    python3-pyyaml

%description -n python3-PyYAML
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistence.

%prep
%autosetup -p1 -n pyyaml-%{version}
chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files yaml _yaml

%files -n python3-PyYAML -f %{pyproject_files}
%doc CHANGES README.md examples

%changelog
%{?autochangelog}
