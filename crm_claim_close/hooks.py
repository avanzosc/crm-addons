# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import logging

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """
    Copy write date to closed date at claim taking into account if the stage is
    closed.
    """
    m_claim = env["crm.claim"]
    claims = m_claim.search([("stage_id.closed", "=", True)])
    if claims:
        _logger.info("Closing claims: %d contracts" % len(claims))
    for claim in claims:
        claim.date_closed = claim.write_date
    _logger.info("Closing claims: Done")
