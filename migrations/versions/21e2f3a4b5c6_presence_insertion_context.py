"""presence insertion context fields

Revision ID: 21e2f3a4b5c6
Revises: 20d1e2f3a4b5
Create Date: 2026-04-02
"""

from alembic import op
import sqlalchemy as sa


revision = "21e2f3a4b5c6"
down_revision = "20d1e2f3a4b5"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("presence_activite", sa.Column("dispositif_type", sa.String(length=120), nullable=True))
    op.add_column("presence_activite", sa.Column("accompagnant_nom", sa.String(length=180), nullable=True))
    op.add_column("presence_activite", sa.Column("accompagnant_type", sa.String(length=30), nullable=True))


def downgrade():
    op.drop_column("presence_activite", "accompagnant_type")
    op.drop_column("presence_activite", "accompagnant_nom")
    op.drop_column("presence_activite", "dispositif_type")
