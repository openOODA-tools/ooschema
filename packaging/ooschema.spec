Name:           ooschema
Version:        0.1.0
Release:        1%{?dist}
Summary:        Infers structural JSON schemas and column datatypes from stream datasets.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooschema
Source0:        ooschema-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooschema is a sovereign, capability-bounded INFER SCHEMA written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooschema
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooschema-uninstall

%files
/usr/bin/ooschema
/usr/bin/ooschema-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
