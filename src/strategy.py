from abc import ABC


class FileSelectionStratgey(ABC):
    """Defines a file selection strategy."""


class OrderedFileSelectionStrategy(FileSelectionStratgey):
    """Selects the PDF files in the order they are recieved."""


class DirectoryFileSelectionStrategy(FileSelectionStratgey):
    """Selects all PDF files in a directory."""


class GUIFileSelectionStrategy(FileSelectionStratgey):
    """Selects all the PDF files using a GUI."""
