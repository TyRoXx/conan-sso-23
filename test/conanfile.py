from conans.model.conan_file import ConanFile
from conans import CMake
import os

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "sso-23/2015.1.29@TyRoXx/master"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(".%sbin%stest " % (os.sep, os.sep))
