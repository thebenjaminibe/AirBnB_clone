#!/usr/bin/env python3
"""Initialize the storage engine"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
