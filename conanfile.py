from contextlib import closing
from tarfile import open as taropen
from urllib2 import urlopen

from conans import ConanFile


class lestConan(ConanFile):
    name = "lest"
    version = "1.26.0"
    url = "https://github.com/martinmoene/lest-conan-package"
    license = "Boost 1.0"
    author = "Martin Moene (martin.moene@gmail.com)"
    settings = None # header-only

    def build(self):
         None #empty too, nothing to build in header only

    def source(self):
        url = "https://github.com/martinmoene/lest/archive/v{0}.tar.gz".format(self.version)
        with closing(urlopen(url)) as dl:
            with taropen(mode='r|gz', fileobj=dl) as archive:
                archive.extractall()

    def package(self):
        self.copy(pattern="*.hpp", dst="include/lest", src="lest-{0}/include/lest".format(self.version))
        # self.copy(pattern="*.hpp", dst="include/lest", src="lest-{0}".format(self.version))

    def package_info(self):
        self.cpp_info.includedirs = ['include/lest']
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
