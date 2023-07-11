from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://94rv29ffg1ld77x6gg8t:pscale_pw_JdrumEXSL5HOy2amDkk2dZqH1bMfBVOSG9hZ4hsIb5k@aws.connect.psdb.cloud/joanncarrers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
     "ssl": {
       "ssl ca": "/etc/ssl/cert.pem"
     }
  })

with engine.connect() as connection:
  result = connection.execute(text("select * from jobs"))
  for row in result:
        print("jobs:", row.title)
 