"""empty message

Revision ID: 900758871713
Revises: ea5a023711e0
Create Date: 2018-05-27 16:36:44.258935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '900758871713'
down_revision = 'ea5a023711e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meta_package',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('provides',
        sa.Column('package_id', sa.Integer(), nullable=False),
        sa.Column('metapackage_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['metapackage_id'], ['meta_package.id'], ),
        sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
        sa.PrimaryKeyConstraint('package_id', 'metapackage_id')
    )
    op.drop_table('harddeps')
    op.drop_table('softdeps')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('softdeps',
        sa.Column('package_id', sa.INTEGER(), nullable=False),
        sa.Column('dependency_id', sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(['dependency_id'], ['package.id'], ),
        sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
        sa.PrimaryKeyConstraint('package_id', 'dependency_id')
    )
    op.create_table('harddeps',
        sa.Column('package_id', sa.INTEGER(), nullable=False),
        sa.Column('dependency_id', sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(['dependency_id'], ['package.id'], ),
        sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
        sa.PrimaryKeyConstraint('package_id', 'dependency_id')
    )
    op.drop_table('provides')
    op.drop_table('meta_package')
    # ### end Alembic commands ###