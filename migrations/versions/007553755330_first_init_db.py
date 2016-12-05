"""first init db

Revision ID: 007553755330
Revises: None
Create Date: 2016-12-05 19:55:32.218000

"""

# revision identifiers, used by Alembic.
revision = '007553755330'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank_bill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('total_exchange', sa.Float(), nullable=True),
    sa.Column('transaction_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clerk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('user_cookies', sa.Text(), nullable=True),
    sa.Column('real_name', sa.String(length=64), nullable=True),
    sa.Column('wallet', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('real_name'),
    sa.UniqueConstraint('username')
    )
    op.create_table('bank_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_bank_bill', sa.Integer(), nullable=True),
    sa.Column('total_money', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_bank_bill'], ['bank_bill.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bank_bill_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.Integer(), nullable=True),
    sa.Column('id_bank_bill', sa.Integer(), nullable=True),
    sa.Column('bank', sa.Integer(), nullable=True),
    sa.Column('serial_number', sa.Integer(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('exchange', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_bank_bill'], ['bank_bill.id'], ),
    sa.ForeignKeyConstraint(['user_name'], ['user.real_name'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('current_usage', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eq_bill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_clerk', sa.Integer(), nullable=True),
    sa.Column('id_equipment', sa.Integer(), nullable=True),
    sa.Column('current_usage', sa.Float(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['current_usage'], ['equipment.current_usage'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_clerk'], ['clerk.id'], ),
    sa.ForeignKeyConstraint(['id_equipment'], ['equipment.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.Integer(), nullable=True),
    sa.Column('clerk_id', sa.Integer(), nullable=True),
    sa.Column('equipment_id', sa.Integer(), nullable=True),
    sa.Column('usage', sa.Float(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['clerk_id'], ['clerk.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['usage'], ['equipment.current_usage'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_name'], ['user.real_name'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company_bill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_bank_bill', sa.Integer(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('money', sa.Float(), nullable=True),
    sa.Column('id_transaction', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_bank_bill'], ['bank_bill.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_transaction'], ['transaction.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company_bill')
    op.drop_table('transaction')
    op.drop_table('eq_bill')
    op.drop_table('equipment')
    op.drop_table('bank_bill_item')
    op.drop_table('bank_account')
    op.drop_table('user')
    op.drop_table('clerk')
    op.drop_table('bank_bill')
    ### end Alembic commands ###
