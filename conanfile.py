from conans import ConanFile

class LabVIEWBuild(ConanFile):
    requires = "labview_conan_poc_libc/[~=0.*]@user/stable"
    python_requires = "labview_conan_extension/[~=0.0.*]@user/stable"
    python_requires_extend = "labview_conan_extension.LabVIEWConanExtension"
    gitURL = "ssh://git@ssh.github.com:443/stefan-lemmens/labview_conan_poc_libb.git"