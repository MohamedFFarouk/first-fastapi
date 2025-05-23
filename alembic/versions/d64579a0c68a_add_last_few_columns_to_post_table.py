"""add last few columns to post table

Revision ID: d64579a0c68a
Revises: a014a583d6d3
Create Date: 2025-05-22 20:16:12.185759

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d64579a0c68a"
down_revision: Union[str, None] = "a014a583d6d3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), server_default="TRUE", nullable=False),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
