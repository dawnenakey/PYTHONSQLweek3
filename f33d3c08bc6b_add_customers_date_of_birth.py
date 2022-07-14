"""add customers date_of_birth

Revision ID: f33d3c08bc6b
Revises: 51e8445370af
Create Date: 2022-06-18 12:15:05.831088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f33d3c08bc6b'
down_revision = '51e8445370af'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
