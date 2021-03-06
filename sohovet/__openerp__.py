# -*- encoding: utf-8 -*-
##############################################################################
#                                                                            #
#  OpenERP, Open Source Management Solution.                                 #
#                                                                            #
#  @author Juan Ignacio Alonso Barba <jialonso@grupovermon.com>              #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.      #
#                                                                            #
##############################################################################

{
    'name': 'SOHOVet master',
    'version': '1.0',
    'category': 'Productos',
    'description': """Módulo que personaliza Odoo para SOHOVet.""",
    'author': 'Juan Ignacio Alonso Barba',
    'website': 'http://www.enzo.es/',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'purchase',
        'sohovet_product',
        'sohovet_import_comments',
        'sohovet_product_price',
        'sohovet_simplified_uom',
        'sohovet_import_supplier_products',
        'sohovet_stock_report',
        'sohovet_purchase_order_report',
        # 'sohovet_animal',
        # 'sohovet_appointment',
        # 'sohovet_connector',
        # 'sohovet_vaccine',
        # 'sohovet_vaccine_call_reminder',
        # 'sohovet_vaccine_textlocal',
        # 'sohovet_related_products',
    ],
    'data': [
        'data/sohovet_warehouse.xml',
        'data/l10n_es_toponyms_states_spanish.xml',
    ],
    # 'qweb': [
    #     'static/src/xml/base.xml',
    # ],
    'active': False,
    'installable': True,
}
