# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-02-18
### Added
- Initial release of the User Management System.
- GUI built with Tkinter.
- SQLite database integration for persistent storage.
- Standalone executable (.exe) for Windows.
- README with installation and download instructions.

### Fixed
- Direct download link in README for better user experience.

## [2.2.3] - 2026-02-22
### Added
- **New UI Engine**: Complete migration from Tkinter to Flet for a modern, cross-platform look.
- **Search Functionality**: Added `search_user_by_name` using SQL `LIKE` for partial name matches.
- **About Dialog**: Implemented `ft.AlertDialog` for app credits and version info.
- **Global Feedback**: Added a dedicated multiline TextField for system messages and user list display.

### Changed
- **Architecture**: Separated GUI and Models logic to prevent circular imports.
- **Delete Logic**: Improved user deletion with input normalization and UI refresh.

### Fixed
- Fixed name conflicts between UI TextFields and Backend functions.
- Resolved "NoneType" error in deletion logic by improving function return values.