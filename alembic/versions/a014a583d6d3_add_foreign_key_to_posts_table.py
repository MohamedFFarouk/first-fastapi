"""add foreign key to posts table

Revision ID: a014a583d6d3
Revises: 4e25050ff820
Create Date: 2025-05-22 20:09:34.840746

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a014a583d6d3"
down_revision: Union[str, None] = "4e25050ff820"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "owner_id",
            sa.Integer(),
            nullable=False,
        ),
    )
    op.create_foreign_key(
        "fk_posts_users", "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE"
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_posts_users", "posts")
    op.drop_column("posts", "owner_id")
