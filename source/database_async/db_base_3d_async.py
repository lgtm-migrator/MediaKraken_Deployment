async def db_3d_list_count(self, search_value=None):
    return 0


async def db_3d_list(self, offset=None, records=None, search_value=None, db_connection=None):
    """
    Return collections list from the database
    """
    if db_connection is None:
        db_conn = self.db_connection
    else:
        db_conn = db_connection
    return None
