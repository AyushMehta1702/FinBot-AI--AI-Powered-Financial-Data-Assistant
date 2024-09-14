from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, LargeBinary

#engine = create_engine(dbname="finance_chatbot", user="postgres", password="001127", host="localhost", port=5432)
engine = create_engine('postgresql://postgres:001127@localhost/finance_chatbot')
metadata = MetaData()

financial_data = Table(
    'financial_data', metadata,
    Column('id', Integer, primary_key=True),
    Column('concatenated', String),
    Column('embedding'),  # or VECTOR if applicable
    extend_existing=True
)
