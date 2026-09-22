# Copyright 2026 AvanzOSC - Lucía Echeverría
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import logging

from odoo.tools.sql import column_exists, table_exists

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    cr = env.cr
    if not table_exists(cr, "crm_causa") or not column_exists(
        cr, "crm_claim", "causa_id"
    ):
        return
    cr.execute("SELECT COUNT(*) FROM crm_claim_description")
    if cr.fetchone()[0]:
        _logger.warning("crm_claim_description is not empty, legacy causes not loaded.")
        return
    cr.execute(
        """
        INSERT INTO crm_claim_description (
            id, name, description, type_description,
            create_uid, create_date, write_uid, write_date
        )
        SELECT id, TRIM(name), TRIM(name), 'cause',
            create_uid, create_date, write_uid, write_date
        FROM crm_causa
        WHERE NULLIF(TRIM(name), '') IS NOT NULL
        """
    )
    loaded = cr.rowcount
    cr.execute(
        """
        SELECT setval(
            pg_get_serial_sequence('crm_claim_description', 'id'),
            GREATEST((SELECT MAX(id) FROM crm_claim_description), 1)
        )
        """
    )
    cr.execute(
        """
        UPDATE crm_claim claim
        SET cause_description_id = claim.causa_id
        FROM crm_claim_description descr
        WHERE descr.id = claim.causa_id
            AND claim.cause_description_id IS NULL
        """
    )
    _logger.info(
        "Loaded %s legacy claim causes and linked %s claims.", loaded, cr.rowcount
    )
    env["crm.claim.description"].invalidate_model()
    env["crm.claim"].invalidate_model(["cause_description_id"])
