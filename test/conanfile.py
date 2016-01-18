from os.path import join
from conans import ConanFile, CMake


class lestPackageTest(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "lest/1.26.0@martin_moene/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(join(".", "bin", "test"))
