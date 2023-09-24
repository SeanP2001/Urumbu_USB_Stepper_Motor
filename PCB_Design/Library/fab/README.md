# Fab Electronics Library for KiCad

This library (should) cover all the electronics components found in the official [fab inventory](http://fab.cba.mit.edu/about/fab/inv.html). Using this library should also make it easier to share KiCad project files between Mac, Windows and Linux systems.

> **Warning!** the library is under active development. Naming of components can change overnight. Make sure to `git pull` the latest version before doing work.

## Installation

> Make sure you have at KiCad 6 or greater installed.

1. Clone or download this repository. You may rename the directory to `fab`.
2. Store it in a safe place such as `~/kicad/libraries` or `C:/kicad/libraries`.
3. Run KiCad or open a KiCad `.pro` file.
4. Go to "Preferences / Manage Symbol Libraries" and add `fab.kicad_sym` as symbol library.
5. Go to "Preferences / Manage Footprint Libraries" and add `fab.pretty` as footprint library.
6. Go to "Preferences / Configure Paths" and add variable named **FAB** that points to the installation directory of the fab library, such as `~/kicad/libraries/fab` or `C:/kicad/libraries/fab`. This will enable the custom 3D shapes to be found. The 3D shapes project has just started and most of them have to be populated still.

## On-Going TODO

- [x] Create a test script that checks if parts from fab inventory are included
- [ ] Make sure all parts from the inventory are there
- [ ] Fix symbols and footprints according to KLC tests using [KiCad Library Utilities](https://gitlab.com/kicad/libraries/kicad-library-utils)
- [ ] Review symbol and footprint local naming conventions

## Contributing

Please refer to the [CONTRIBUTING](CONTRIBUTING.md) document. Run `test.py` locally before `git push`.

## License

Please refer to the [LICENSE](LICENSE) document located in this repository.
