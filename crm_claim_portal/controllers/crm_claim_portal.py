
from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id

        claim_obj = request.env['crm.claim']
        if 'claim_count' in counters:
            values['claim_count'] = (
                claim_obj.search_count([
                    ('commercial_partner_id', 'child_of',
                     [partner.commercial_partner_id.id]),
                ]) if claim_obj.check_access_rights(
                    'read', raise_exception=False) else 0)
        return values

    def _claim_get_page_view_values(self, claim, access_token, **kwargs):
        values = {
            'page_name': 'claim',
            'claim': claim,
        }
        return self._get_page_view_values(
            claim, access_token, values, 'my_claims_history', False, **kwargs)

    @http.route(['/my/claims', '/my/claims/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_my_claims(
            self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        claim_obj = request.env['crm.claim']
        domain = []

        searchbar_sortings = {
            "date": {
                "label": _('Newest'),
                "order": "create_date desc"
            },
            "name": {
                "label": _("Name"),
                "order": "name"
            },
        }
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        if date_begin and date_end:
            domain += [("create_date", '>', date_begin),
                       ("create_date", '<=', date_end)]

        # projects count
        claim_count = claim_obj.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/claims",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby
            },
            total=claim_count,
            page=page,
            step=self._items_per_page
        )

        # content according to pager and archive selected
        claims = claim_obj.search(
            domain, order=order, limit=self._items_per_page,
            offset=pager['offset'])
        request.session["my_claims_history"] = claims.ids[:100]

        values.update({
            "date": date_begin,
            "date_end": date_end,
            "claims": claims,
            "page_name": 'claim',
            "default_url": '/my/claims',
            "pager": pager,
            "searchbar_sortings": searchbar_sortings,
            'sortby': sortby
        })
        return request.render("crm_claim_portal.portal_my_claims", values)

    @http.route(["/my/claim/<int:claim_id>"],
                type="http", auth="public", website=True)
    def portal_my_claim(self, claim_id=None, access_token=None, **kw):
        try:
            claim_sudo = self._document_check_access(
                "crm.claim", claim_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        values = self._claim_get_page_view_values(
            claim_sudo, access_token, **kw)
        return request.render("crm_claim_portal.portal_my_claim", values)
