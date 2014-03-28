from openerp.osv import osv, fields
from openerp.tools.translate import _

class res_partner(osv.Model):

    _name = "res.partner"
    _inherit = "res.partner"
    _columns = {
        'exact_supplier_number': fields.boolean('Exact Supplier Number', help="Flagging this field will limit the voucher lines in your bank statement to the OBI reference provided."),
    }