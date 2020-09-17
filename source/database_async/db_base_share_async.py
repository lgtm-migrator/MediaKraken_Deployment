import uuid


async def db_share_add(self, share_type, share_user, share_password, share_server,
                       share_path, db_connection=None):
    """
    # add share path
    """
    if db_connection is None:
        db_conn = self.db_connection
    else:
        db_conn = db_connection
    new_guid = str(uuid.uuid4())
    await self.db_connection.execute('insert into mm_media_share (mm_media_share_guid,'
                                     ' mm_media_share_type,'
                                     ' mm_media_share_user,'
                                     ' mm_media_share_password,'
                                     ' mm_media_share_server,'
                                     ' mm_media_share_path)'
                                     ' values ($1, $2, $3, $4, $5, $6)',
                                     new_guid, share_type, share_user,
                                     share_password, share_server, share_path)
    return new_guid


async def db_share_check(self, dir_path, db_connection=None):
    """
    # share path check (dupes)
    """
    if db_connection is None:
        db_conn = self.db_connection
    else:
        db_conn = db_connection
    return await self.db_connection.fetchval(
        'select count(*) from mm_media_share where mm_media_share_path = $1',
        dir_path)


async def db_share_delete(self, share_guid, db_connection=None):
    """
    # remove share
    """
    if db_connection is None:
        db_conn = self.db_connection
    else:
        db_conn = db_connection
    await self.db_connection.execute('delete from mm_media_share where mm_media_share_guid = $1',
                                     share_guid)


async def db_share_list(self, offset=0, records=None, db_connection=None):
    """
    # read the shares list
    """
    if db_connection is None:
        db_conn = self.db_connection
    else:
        db_conn = db_connection
    return await self.db_connection.fetch('select mm_media_share_guid,'
                                          ' mm_media_share_type,'
                                          ' mm_media_share_user,'
                                          ' mm_media_share_password,'
                                          ' mm_media_share_server,'
                                          ' mm_media_share_path'
                                          ' from mm_media_share'
                                          ' order by mm_media_share_type, mm_media_share_server,'
                                          ' mm_media_share_path offset $1 limit $2',
                                          offset, records)


async def db_share_update_by_uuid(self, share_type, share_user, share_password,
                                  share_server,
                                  share_path, share_id, db_connection=None):
    """
    # update share
    """
    if db_connection is None:
        db_conn = self.db_connection
    else:
        db_conn = db_connection
    await self.db_connection.execute('update mm_media_share set mm_media_share_type = $1,'
                                     ' mm_media_share_user = $2,'
                                     ' mm_media_share_password = $3',
                                     ' mm_media_share_server = $4',
                                     ' where mm_media_share_path = $5',
                                     ' and mm_media_share_guid = $6',
                                     share_type, share_user,
                                     share_password, share_server,
                                     share_path, share_id)
