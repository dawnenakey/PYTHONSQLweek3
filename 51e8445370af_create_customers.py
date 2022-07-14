"""create customers

Revision ID: 51e8445370af
Revises: 
Create Date: 2022-06-18 12:04:52.983124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51e8445370af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
