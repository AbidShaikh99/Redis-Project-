"""empty message

Revision ID: 694adc6180ca
Revises: a414e24dada8
Create Date: 2026-04-24 12:34:39.470766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '694adc6180ca'
down_revision: Union[str, Sequence[str], None] = 'a414e24dada8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
