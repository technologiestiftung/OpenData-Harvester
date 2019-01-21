import connect
import models

models.meta_helper.metadata.create_all(connect.get_connection())
