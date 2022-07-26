from operator import itemgetter

from dateutil.relativedelta import relativedelta

from odoo import _, fields, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.osv.expression import OR
from odoo.tools import date_utils, groupby as groupbyelem

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class CustomerPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        if "claim_count" in counters:
            values["claim_count"] = request.env["crm.claim"].search_count([])
        return values

    def _claim_get_page_view_values(self, claim, access_token, **kwargs):
        values = {
            "page_name": "claim",
            "claim": claim,
        }
        return self._get_page_view_values(
            claim, access_token, values, "my_claims_history", False, **kwargs
        )

    def _get_searchbar_sortings(self):
        return {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {
                "label": _("Name"),
                "order": "name",
            },
            "deadline": {
                "label": _("Deadline"),
                "order": "date_deadline desc",
            },
        }

    def _get_searchbar_filters(self):
        today = fields.Date.today()
        quarter_start, quarter_end = date_utils.get_quarter(today)
        last_week = today + relativedelta(weeks=-1)
        last_month = today + relativedelta(months=-1)
        last_year = today + relativedelta(years=-1)

        return {
            "all": {
                "label": _("All"),
                "domain": [],
            },
            "open": {
                "label": _("Open"),
                "domain": [("date_closed", "=", False)],
            },
            "close": {
                "label": _("Closed"),
                "domain": [("date_closed", "!=", False)],
            },
            "today": {
                "label": _("Today"),
                "domain": [("create_date", "=", today)],
            },
            "week": {
                "label": _("This week"),
                "domain": [
                    ("create_date", ">=", date_utils.start_of(today, "week")),
                    ("create_date", "<=", date_utils.end_of(today, "week")),
                ],
            },
            "month": {
                "label": _("This month"),
                "domain": [
                    ("create_date", ">=", date_utils.start_of(today, "month")),
                    ("create_date", "<=", date_utils.end_of(today, "month")),
                ],
            },
            "year": {
                "label": _("This year"),
                "domain": [
                    ("create_date", ">=", date_utils.start_of(today, "year")),
                    ("create_date", "<=", date_utils.end_of(today, "year")),
                ],
            },
            "quarter": {
                "label": _("This Quarter"),
                "domain": [
                    ("create_date", ">=", quarter_start),
                    ("create_date", "<=", quarter_end),
                ],
            },
            "last_week": {
                "label": _("Last week"),
                "domain": [
                    ("create_date", ">=", date_utils.start_of(last_week, "week")),
                    ("create_date", "<=", date_utils.end_of(last_week, "week")),
                ],
            },
            "last_month": {
                "label": _("Last month"),
                "domain": [
                    ("create_date", ">=", date_utils.start_of(last_month, "month")),
                    ("create_date", "<=", date_utils.end_of(last_month, "month")),
                ],
            },
            "last_year": {
                "label": _("Last year"),
                "domain": [
                    ("create_date", ">=", date_utils.start_of(last_year, "year")),
                    ("create_date", "<=", date_utils.end_of(last_year, "year")),
                ],
            },
        }

    def _get_searchbar_inputs(self):
        return {
            "content": {
                "input": "content",
                "label": _("Search <span class='nolabel'> (in Content)</span>"),
            },
            "message": {
                "input": "message",
                "label": _("Search in Messages"),
            },
            "stage": {
                "input": "stage",
                "label": _("Search in Stages"),
            },
            "all": {
                "input": "all",
                "label": _("Search in All"),
            },
        }

    def _get_searchbar_groupby(self):
        return {
            "none": {
                "input": "none",
                "label": _("None"),
            },
            "stage": {
                "input": "stage",
                "label": _("Stage"),
            },
            "partner": {
                "input": "partner",
                "label": _("Reported by"),
            },
            "user": {
                "input": "user",
                "label": _("Assigned to"),
            },
        }

    @http.route(
        ["/my/claims", "/my/claims/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_claims(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        groupby=None,
        **kw
    ):
        values = self._prepare_portal_layout_values()
        claim_obj = request.env["crm.claim"]

        searchbar_sortings = self._get_searchbar_sortings()
        searchbar_filters = self._get_searchbar_filters()
        searchbar_inputs = self._get_searchbar_inputs()
        searchbar_groupby = self._get_searchbar_groupby()

        # default sort by value
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]

        # default filter by value
        if not filterby:
            filterby = "all"
        domain = searchbar_filters.get(filterby, searchbar_filters.get("all"))["domain"]

        # default group by value
        if not groupby:
            groupby = "none"

        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]

        # search
        if search and search_in:
            search_domain = []
            if search_in in ("content", "all"):
                search_domain = OR(
                    [
                        search_domain,
                        [
                            "|",
                            ("name", "ilike", search),
                            ("description", "ilike", search),
                        ],
                    ]
                )
            if search_in in ("message", "all"):
                search_domain = OR(
                    [search_domain, [("message_ids.body", "ilike", search)]]
                )
            if search_in in ("stage", "all"):
                search_domain = OR([search_domain, [("stage_id", "ilike", search)]])
            domain += search_domain

        # projects count
        claim_count = claim_obj.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/claims",
            url_args={
                "date_begin": date_begin,
                "date_end": date_end,
                "sortby": sortby,
                "filterby": filterby,
                "groupby": groupby,
                "search_in": search_in,
                "search": search,
            },
            total=claim_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        if groupby == "stage":
            order = "stage_id, %s" % order
            # force sort on stage first to group by stage in view
        elif groupby == "partner":
            order = "partner_id, %s" % order
            # force sort on partner first to group by partner in view
        elif groupby == "user":
            order = "user_id, %s" % order
            # force sort on user first to group by user in view

        claims = claim_obj.search(
            domain, order=order, limit=self._items_per_page, offset=pager["offset"]
        )
        request.session["my_claims_history"] = claims.ids[:100]

        if groupby == "stage":
            grouped_claims = [
                request.env["crm.claim"].concat(*g)
                for k, g in groupbyelem(claims, itemgetter("stage_id"))
            ]
        elif groupby == "partner":
            grouped_claims = [
                request.env["crm.claim"].concat(*g)
                for k, g in groupbyelem(claims, itemgetter("partner_id"))
            ]
        elif groupby == "user":
            grouped_claims = [
                request.env["crm.claim"].concat(*g)
                for k, g in groupbyelem(claims, itemgetter("user_id"))
            ]
        else:
            grouped_claims = [claims]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "grouped_claims": grouped_claims,
                "page_name": "claim",
                "default_url": "/my/claims",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "searchbar_groupby": searchbar_groupby,
                "searchbar_inputs": searchbar_inputs,
                "search_in": search_in,
                "search": search,
                "sortby": sortby,
                "groupby": groupby,
                "searchbar_filters": searchbar_filters,
                "filterby": filterby,
            }
        )
        return request.render("crm_claim_portal.portal_my_claims", values)

    @http.route(["/my/claim/<int:claim_id>"], type="http", auth="public", website=True)
    def portal_my_claim(self, claim_id, access_token=None, **kw):
        try:
            claim_sudo = self._document_check_access(
                "crm.claim", claim_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._claim_get_page_view_values(claim_sudo, access_token, **kw)
        return request.render("crm_claim_portal.portal_my_claim", values)
