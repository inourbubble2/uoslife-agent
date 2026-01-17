"""change_embedding_id_to_uuid

Revision ID: 7f12a8f6cbf9
Revises: 93e67fc66005
Create Date: 2026-01-17 11:50:56.833474

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7f12a8f6cbf9"
down_revision: str | Sequence[str] | None = "93e67fc66005"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TABLE announcement_embedding ALTER COLUMN id DROP DEFAULT")
    op.alter_column(
        "announcement_embedding",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.UUID(),
        existing_nullable=False,
        postgresql_using="gen_random_uuid()",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "announcement_embedding", "id", existing_type=sa.UUID(), type_=sa.INTEGER(), existing_nullable=False
    )
