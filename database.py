from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://dzz718f3s2105wfmun4h:pscale_pw_niVSw4KIq0klhFFZ1EDRm4ALznTep8uWCI8IhFhS6rL@aws.connect.psdb.cloud/joanncarrers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select *from jobs"))
  print(result.all())
