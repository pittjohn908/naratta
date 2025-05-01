"""init

Revision ID: 87884589a8a0
Revises: 
Create Date: 2025-05-01 11:04:34.086893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87884589a8a0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # """Upgrade schema."""
    op.create_table(
        "novels",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("author", sa.String(200), nullable=False),
    )

    op.create_table(
        "characters",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("novel_id", sa.Integer, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("metadata", sa.JSON),
        sa.ForeignKeyConstraint(
            ["novel_id"],
            ["novels.id"],
            name="fk_character_novel_id",
        ),
    )

    op.create_index("ik_author", "novels", ["author"], unique=False)
    op.create_index("ik_character_novel_id", "characters", ["novel_id"], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("ik_character_novel_id", "characters")
    op.drop_index("ik_author", "novels")
    op.drop_constraint("fk_character_novel_id", "characters", type_="foreignkey")
    op.drop_table("characters")
    op.drop_table("novels")
