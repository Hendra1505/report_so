# -*- coding: utf-8 -*-

from odoo import models, fields, api

import time
import logging
_logger = logging.getLogger(__name__)


class sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    description = fields.Char(string="Deskripsi")
    image = fields.Image(string="Image")
    e_signature = fields.Binary(string="Signature")
