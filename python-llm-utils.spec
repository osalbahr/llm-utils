Name:           python-llm-utils
Version:        0.2.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Utilities for our LLM projects (CWhy, ChatDBG, ...).

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/plasma-umass/llm-utils
Source:         %{pypi_source llm_utils}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'llm-utils' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-llm-utils
Summary:        %{summary}

%description -n python3-llm-utils %_description


%prep
%autosetup -p1 -n llm_utils-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ...


%check
%pyproject_check_import


%files -n python3-llm-utils -f %{pyproject_files}


%changelog
%autochangelog