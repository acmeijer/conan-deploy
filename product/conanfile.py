from conans import ConanFile, CMake

class ProductConan(ConanFile):
    name = 'Product'
    version = '1.0.0'

    def requirements(self):
        self.requires.add('AppA/1.0.0')
        self.requires.add('AppB/1.0.0')
