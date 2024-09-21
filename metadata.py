from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, LargeBinary


engine = create_engine('postgresql://postgres:password@localhost/dbname')
metadata = MetaData()

financial_data = Table(
    'financial_data', metadata,
    Column('id', Integer, primary_key=True),
    Column('concatenated', String),
    Column('embedding'),  # or VECTOR if applicable
    extend_existing=True
)
