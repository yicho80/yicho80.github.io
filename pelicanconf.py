#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'yicho80'
SITENAME = 'The World In a Nutshell'
SITEURL = ''

PATH = 'content'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 3
DEFAULT_DATE_FORMAT = ('%Y-%b-%d')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud", "neighbors"]

# Theme
THEME = 'theme'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DISQUS_SITENAME = 'yicho80-github-io'