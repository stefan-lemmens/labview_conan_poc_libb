from conans import ConanFile

class LabVIEWBuild(ConanFile):
    requires = "labview_conan_poc_libc/[~=0.*]@intersoft/testing"
    python_requires = "labview_conan_extension/[~=20.0.*]@intersoft/stable"
    python_requires_extend = "labview_conan_extension.LabVIEWConanExtension"
    gitURL = "ssh://git@bitbucket.atlassian.inventive-engineering.com:7999/~stefan/labview_conan_poc_libb.git"