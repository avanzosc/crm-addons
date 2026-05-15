import logging

from odoo import _

_logger = logging.getLogger(__name__)


def _post_install_put_department_in_claims(env):
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
