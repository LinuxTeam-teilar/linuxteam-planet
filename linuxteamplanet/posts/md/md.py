#  Copyright 2012 by Giorgos Tsiapaliokas <terietor@gmail.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; see the file COPYING.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.

from os import path, walk
import fnmatch
import logging
import markdown

# Get an instance of a logger
logger = logging.getLogger(__name__)

class MD(object):
    def __init__(self, source_path):
        self._source = source_path

    @property
    def elements(self):
        dataList = []
        for root, dirnames, filenames in walk(self._source):
            for filename in fnmatch.filter(filenames, '*.md'):
                l = root.split('_')

                date = l[0]
                post_id = l[1]
                markdown_text = ''
                with open(path.join(root, filename)) as f:
                    markdown_text = f.read()

                html = markdown.markdown(markdown_text)
                data = {
                    "author": 'LinuxTeam Teilar',
                    "link": post_id,
                    "content": html,
                    "date": date,
                    "isInternalPost": True
                }
                dataList.append(data)
        return dataList


