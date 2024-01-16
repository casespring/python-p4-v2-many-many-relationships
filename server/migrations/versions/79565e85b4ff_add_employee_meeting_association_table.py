"""add employee_meeting association table

Revision ID: 79565e85b4ff
Revises: 48c20f514f17
Create Date: 2024-01-16 14:22:55.443543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79565e85b4ff'
down_revision = '48c20f514f17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees_meeetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employees_meeetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], name=op.f('fk_employees_meeetings_meeting_id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'meeting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_meeetings')
    # ### end Alembic commands ###
