# *lest* conan package

This is a [Conan.io](https://www.conan.io/) package for the [*lest*](https://github.com/martinmoene/lest) header-only C++11 unit-testing framework.

The packages generated with this *conanfile* can be found in [conan.io](https://conan.io/source/lest/1.26.0/martinmoene/stable).

**Contents**
- [Test the package](#test-the-package)
- [Upload the package to the conan server](#upload-the-package-to-the-conan-server)
- [Use the package](#use-the-package)


## Test the package

### Prepare the local conan server

Add write permission to server configuration file, `~/.conan_server/server.conf`:

	[write_permissions]
	*/*@*/*: *

Start the local conan server:

	$ conan_server &

### Upload the package to the local conan server

	$ conan user demo
	$ conan export martin_moene/stable
	$ conan install lest/1.26.0@martin_moene/stable --build
	$ conan upload lest/1.26.0@martin_moene/stable --all -r=local
	# pw: demo

### Perform the package test

	$ conan test

## Upload the package to the conan server

	$ conan user martin_moene
	$ conan export martin_moene/stable
	$ conan install lest/1.26.0@martin_moene/stable --build
    $ conan upload lest/1.26.0@martin_moene/stable --all

## Use the package

### Basic setup

    $ conan install lest/1.26.0@martin_moene/stable
    
### Project setup

In a *conanfile.txt* file:

    [requires]
    lest/1.26.0@martin_moene/stable

    [generators]
    txt
    cmake

With multiple dependencies in your project it is better to use a *conanfile.py* file. See for example the [package test *conanfile.py* file](test/conanfile.py).
    
Complete the installation of requirements for your project running:

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
