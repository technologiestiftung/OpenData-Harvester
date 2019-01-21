import connect
import models

models.meta.metadata.create_all(connect.get_connection())
