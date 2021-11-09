DB_HOST="postgresql://localhost:5432"
DB_NAME="postgres"
DB_USER="userrootpostgresql"
DB_PASS="arjit"

import psycopg2

conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)

cur=conn.cursor()


