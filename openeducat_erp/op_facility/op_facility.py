# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields


class op_facility(models.Model):
    _name = 'op.facility'
    _rec_name = 'Name'

    Name = fields.Char('Name', size=16, required=True)
    Code = fields.Char('Code', size=4, required=True)
    hostel_room_id = fields.Many2one('op.hostel.room', 'Hostel Room')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
