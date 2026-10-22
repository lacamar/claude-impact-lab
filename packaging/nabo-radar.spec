Name:           nabo-radar
Version:        0.1.0
Release:        1%{?dist}
Summary:        Collect and tag upcoming Oslo events for Nabo

License:        MIT
URL:            https://github.com/lacamar/claude-impact-lab
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  tzdata
BuildRequires:  systemd-rpm-macros
Requires:       python3
Requires:       tzdata

%description
Scrapes structured event feeds from Oslo venues and ticket sites into SQLite
and tags them with a local language model.

%prep
%autosetup

%build

%install
install -Dm644 radar/sources.py %{buildroot}%{_datadir}/%{name}/sources.py
install -Dm755 radar/radar.py %{buildroot}%{_datadir}/%{name}/radar.py
install -d %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/radar.py %{buildroot}%{_bindir}/%{name}
install -Dm644 radar/systemd/nabo-radar.service %{buildroot}%{_userunitdir}/nabo-radar.service
install -Dm644 radar/systemd/nabo-radar.timer %{buildroot}%{_userunitdir}/nabo-radar.timer

%check
cd radar && python3 test_radar.py

%post
%systemd_user_post nabo-radar.timer

%preun
%systemd_user_preun nabo-radar.timer

%postun
%systemd_user_postun_with_restart nabo-radar.timer

%files
%doc radar/README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_userunitdir}/nabo-radar.service
%{_userunitdir}/nabo-radar.timer

%changelog
* to. okt. 22 2026 lacamar <lchlnm@pm.me> - 0.1.0-1
- Initial package
