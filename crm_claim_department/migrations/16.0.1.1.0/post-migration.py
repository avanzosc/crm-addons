import logging

from openupgradelib import openupgrade

from odoo import _

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    cond = [("user_id", "!=", False), ("department_id", "=", False)]
    claims = env["crm.claim"].search(cond)
    for claim in claims:
        try:
            claim.department_id = claim.user_id._search_user_department()
        except Exception:
            _logger.error = _(
                "Error processing claim: %(claim_name)s, for put department"
            ) % {
                "claim_name": claim.name,
            }
