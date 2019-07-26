# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AuthorNacimiento(models.Model):
    # Modulo del que heredamos
    _inherit = "author"

    lugar_nacimiento = fields.Char(string="Lugar de nacimiento")


class DiscGenere(models.Model):
    # Modulo del que heredamos
    _inherit = "disc"

    # Importante poner las letras de cadad opcion en orden
    genere = fields.Selection([("a", "Rock"), ("b", "Pop"), ("c", "Pop-Rock"), ("d", "Heavy")])
