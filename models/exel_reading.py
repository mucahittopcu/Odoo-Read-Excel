from collections import OrderedDict
from odoo import fields, models, api
from pyexcel_ods import get_data


class Building(models.Model):
    _name = 'excel.list'
    _description = 'Liste'

    name = fields.Char(string='Name')
    surname = fields.Char(string='Surname')
    city = fields.Char(string='City')
    age = fields.Integer(string='Age')

    @api.multi
    def unlink(self):
        return super(Building, self).unlink()

    @api.multi
    def read_show(self):
        data = get_data("/opt/odoo12/custom-addons/read_xls/source/list.ods")
        data = data['Sheet1']
        for i in range(len(data)):
            cause_id = self.env['excel.list'].create({
                'name': data[i][0],
                'surname': data[i][1],
                'city': data[i][2],
                'age': data[i][3]
            })
        find_id = self.env["excel.list"].search([('age', '=', '0')]).unlink()

        wt = self.env['excel.list']
        id_needed = wt.search([('age', '=', '0')]).id
        new = wt.browse(id_needed)
        print(new.name)
