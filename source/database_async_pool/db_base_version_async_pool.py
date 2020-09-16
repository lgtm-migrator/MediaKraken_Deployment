async def db_version_check(db_connection):
    """
    query db version
    """
    return db_connection.fetchval('select mm_version_no'
                                  ' from mm_version')
