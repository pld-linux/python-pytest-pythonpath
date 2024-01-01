#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (obsolete with pytest 7)

Summary:	pytest plugin for adding to the PYTHONPATH from command line or configs
Summary(pl.UTF-8):	Wtyczka pytesta rozszerzająca PYTHONPATH z linii poleceń lub konfiguracji
Name:		python-pytest-pythonpath
Version:	0.7.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-pythonpath/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-pythonpath/pytest-pythonpath-%{version}.tar.gz
# Source0-md5:	8613c4add916c576f6216375ec97af85
URL:		https://pypi.org/project/pytest-pythonpath/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 2.5.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 2.5.2
BuildRequires:	python3-pytest < 7
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a py.test plugin for adding to the PYTHONPATH from the
pytest.ini file before tests run.

%description -l pl.UTF-8
To wtyczka modułu py.test rozszerzania PYTHONPATH na podstawie pliku
pytest.ini przed uruchomieniem testów.

%package -n python3-pytest-pythonpath
Summary:	pytest plugin for adding to the PYTHONPATH from command line or configs
Summary(pl.UTF-8):	Wtyczka pytesta rozszerzająca PYTHONPATH z linii poleceń lub konfiguracji
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pytest-pythonpath
This is a py.test plugin for adding to the PYTHONPATH from the
pytest.ini file before tests run.

%description -n python3-pytest-pythonpath -l pl.UTF-8
To wtyczka modułu py.test rozszerzania PYTHONPATH na podstawie pliku
pytest.ini przed uruchomieniem testów.

%prep
%setup -q -n pytest-pythonpath-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_pythonpath \
%{__python} -m pytest test_pythonpath.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_pythonpath \
%{__python3} -m pytest test_pythonpath.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{py_sitescriptdir}/pytest_pythonpath.py[co]
%{py_sitescriptdir}/pytest_pythonpath-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-pythonpath
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{py3_sitescriptdir}/pytest_pythonpath.py
%{py3_sitescriptdir}/__pycache__/pytest_pythonpath.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_pythonpath-%{version}-py*.egg-info
%endif
