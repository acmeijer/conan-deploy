from conans import ConanFile, CMake

class AppAConan(ConanFile):
    name = 'AppA'
    version = '1.0.0'

    # Requirements listed here are internal to the applications and there is no requirement
    # that these are kept consistent across applications
    def build_requirements(self):
        self.build_requires.add('LibB/1.0.0')

    # Requirements listed here should be kept consistent in the product
    # These might contain common interfaces which are important to be kept the same
    # across multiple applications
    def requirements(self):
        self.requires.add('LibA/1.0.0')
