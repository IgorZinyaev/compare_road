# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CompareRoads
                                 A QGIS plugin
 This plugin compares two linear shapefiles 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-03-09
        copyright            : (C) 2025 by Igor Zinyaev
        email                : igor.zinyaev@yandex.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CompareRoads class from file CompareRoads.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .compare_road import CompareRoads
    return CompareRoads(iface)
