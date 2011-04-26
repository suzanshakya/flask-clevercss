# -*- coding: utf-8 -*-
"""
    flaskext.clevercss
    ~~~~~~~~~~~~~

    A small Flask extension that makes it easy to use cleverCSS with your Flask
    application.

    :copyright: (c) 2010 by Steve Losh.
    :copyright: (c) 2011 by Sujan Shakya.
    :license: MIT, see LICENSE for more details.
"""

import os, subprocess

def clevercss(app):
    @app.before_request
    def _render_clever_css():
        static_dir = app.root_path + app.static_path

        clever_paths = []
        for path, subdirs, filenames in os.walk(static_dir):
            clever_paths.extend([
                os.path.join(path, f)
                for f in filenames if os.path.splitext(f)[1] == '.ccss'
            ])
        for clever_path in clever_paths:
            css_path = os.path.splitext(clever_path)[0] + '.css'
            if not os.path.isfile(css_path):
                css_mtime = -1
            else:
                css_mtime = os.path.getmtime(css_path)
            clever_mtime = os.path.getmtime(clever_path)
            if clever_mtime >= css_mtime:
                subprocess.call(['python', '~/bin/clevercss', clever_path])
