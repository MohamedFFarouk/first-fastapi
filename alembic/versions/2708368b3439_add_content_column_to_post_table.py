"""add content column to post table:

Revision ID: 2708368b3439
Revises: efbe1056785b
Create Date: 2025-05-22 19:49:40.962007

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2708368b3439"
down_revision: Union[str, None] = "efbe1056785b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
