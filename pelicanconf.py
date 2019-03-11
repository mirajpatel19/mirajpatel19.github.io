#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Miraj Patel'
SITENAME = "Miraj's Portfolio"
SITEURL = ''

#-------------------------------------------------

SITETITLE = 'Miraj Patel'
SITESUBTITLE = 'The minimalist Pelican theme'
SITEDESCRIPTION = 'Patel - The minimalist Pelican theme.'
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = '../'
#-------------------------------------------------

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
#___________________________________________________
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
#___________________________________________________


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"] 

# Setting my theme
#THEME = '/path/to/pelican-alchemy/alchemy'
#THEME = 'themes/pelican-alchemy/alchemy'

# To use mnmlist theme. working one!
THEME = "./themes/pelican-themes/Flex"


#THEME = "./themes/pelican-themes/clean-blog"


