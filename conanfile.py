from conans import ConanFile
import os
from conans.tools import download, unzip, check_sha256
from conans import CMake

class ArbitraryName(ConanFile):
    name = "sso-23"
    version = "2015.1.29"
    branch = "master"
    generators = "cmake"
    license = "Boost"
    url="http://github.com/TyRoXx/conan-sso-23"
    ZIP_FOLDER_NAME = "SSO-23-533e88bb9f6e7f6023beeede2b00b0b0f3f6b4ae"

    def source(self):
        zip_name = "sso-23.zip"
        download("https://github.com/elliotgoodrich/SSO-23/archive/533e88bb9f6e7f6023beeede2b00b0b0f3f6b4ae.zip", zip_name)
        check_sha256(zip_name, "701b1d2396bf17b7d8473bab2f955a351603cd407db3626c2e5105ef209b6724")
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("*.hpp", "include", "%s/include" % self.ZIP_FOLDER_NAME, keep_path=True)
