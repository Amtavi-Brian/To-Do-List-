from alembic import op
import sqlalchemy as sa

"""make created_at required

Revision ID: 1aae3b7f3ac6
Revises: 451da1be718a
Create Date: 2026-09-03 11:03:21.817390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1aae3b7f3ac6'
down_revision: Union[str, Sequence[str], None] = '451da1be718a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "todos",
        "created_at",
        existing_type=sa.DateTime(),
        nullable=False
    )


def downgrade() -> None:
    op.alter_column(
        "todos",
        "created_at",
        existing_type=sa.DateTime(),
        nullable=True
    )
