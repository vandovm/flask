"""minha primeira migrate

Revision ID: 88729aa48882
Revises: 
Create Date: 2024-11-26 19:15:16.523516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88729aa48882'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contatos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_msg', sa.DateTime(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('assunto', sa.String(), nullable=True),
    sa.Column('mensagem', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contatos')
    # ### end Alembic commands ###