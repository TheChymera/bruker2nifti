from subprocess import check_output


__author__     = "SebastianoF"
__licence__    = "MIT"
__repository__ = "https://github.com/SebastianoF/bruker2nifti"
__all__ = ['_cores', '_getters', '_utils', 'converter', 'open_GUI']

# Describe the version relative to last tag
command_git = ['git', 'describe', '--match', 'v[0-9]*']
version_buf = check_output(command_git).rstrip()

# Exclude the 'v' for PEP440 conformity, see
# https://www.python.org/dev/peps/pep-0440/#public-version-identifiers
__version__ = version_buf[1:]
