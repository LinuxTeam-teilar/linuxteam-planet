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

from os import path
import json
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Feeds(object):
    def __init__(self, feedsConfigFile):
        with open(feedsConfigFile) as f:
            self.json = json.load(f)

        self._getData()

    def _getData(self):
        elements = self.json["Configs"]["feeds"]
        for element in elements:
            logger.debug(element["source"])
            logger.debug(element["author"] + '\n' + '\n')
