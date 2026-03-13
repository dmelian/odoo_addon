from odoo.addons.portal.controllers.portal import CustomerPortal

class AddonPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values= super()._prepare_home_portal_values(counters)
        values['addon02_count'] = 0
        return values
