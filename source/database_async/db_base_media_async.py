import datetime
import json


async def db_media_duplicate(self, db_connection, offset=0, records=None):
    """
    # list duplicates
    """
    # TODO technically this will "dupe" things like subtitles atm, so group by class guid?
    return await db_connection.fetch('select mm_media_metadata_guid,'
                                     'mm_media_name,'
                                     'count(*)'
                                     ' from mm_media, mm_metadata_movie'
                                     ' where mm_media_metadata_guid is not null'
                                     ' and mm_media_metadata_guid = mm_metadata_guid'
                                     ' group by mm_media_metadata_guid,'
                                     ' mm_media_name HAVING count(*) > 1 order by LOWER(mm_media_name)'
                                     ' offset $1 limit $2', offset, records)


async def db_media_duplicate_count(self, db_connection):
    """
    # count the duplicates for pagination
    """
    # TODO technically this will "dupe" things like subtitles atm
    # TODO perhaps group by classid?
    return await db_connection.fetchval('select count(*) from (select mm_media_metadata_guid'
                                        ' from mm_media'
                                        ' where mm_media_metadata_guid is not null'
                                        ' group by mm_media_metadata_guid HAVING count(*) > 1) as total')


async def db_media_duplicate_detail(self, db_connection, guid, offset=0, records=None):
    """
    # list duplicate detail
    """
    return await db_connection.fetch('select mm_media_guid,'
                                     'mm_media_path,'
                                     'mm_media_ffprobe_json'
                                     ' from mm_media where mm_media_guid'
                                     ' in (select mm_media_guid from mm_media'
                                     ' where mm_media_metadata_guid = $1 offset $2 limit $3)',
                                     guid, offset, records)


async def db_media_duplicate_detail_count(self, db_connection, guid):
    """
    # duplicate detail count
    """
    return await db_connection.fetchval('select count(*) from mm_media'
                                        ' where mm_media_metadata_guid = $1',
                                        guid)


async def db_media_ffprobe_all_guid(self, db_connection, media_uuid, media_class_uuid):
    """
    # fetch all media with METADATA match
    """
    return await db_connection.fetch(
        'select distinct mm_media_guid,'
        'mm_media_ffprobe_json'
        ' from mm_media, mm_metadata_movie'
        ' where mm_media_metadata_guid = '
        '(select mm_media_metadata_guid'
        ' from mm_media where mm_media_guid = $1)'
        ' and mm_media_class_guid = $2',
        media_uuid, media_class_uuid)


async def db_media_insert(self, db_connection, media_uuid, media_path, media_class_uuid,
                          media_metadata_uuid, media_ffprobe_json, media_json):
    """
    # insert media into database
    """
    await db_connection.execute('insert into mm_media (mm_media_guid,'
                                ' mm_media_class_guid,'
                                ' mm_media_path,'
                                ' mm_media_metadata_guid,'
                                ' mm_media_ffprobe_json,'
                                ' mm_media_json)'
                                ' values ($1, $2, $3, $4, $5, $6)',
                                media_uuid, media_class_uuid, media_path,
                                media_metadata_uuid, media_ffprobe_json, media_json)


async def db_media_known(self, db_connection, offset=0, records=None):
    """
    # find all known media
    """
    return await db_connection.fetch('select mm_media_path'
                                     ' from mm_media where mm_media_guid'
                                     ' in (select mm_media_guid'
                                     ' from mm_media order by mm_media_path'
                                     ' offset $1 limit $2) order by mm_media_path',
                                     offset, records)


async def db_media_known_count(self, db_connection):
    """
    # count known media
    """
    return await db_connection.fetchval('select count(*) from mm_media')


async def db_media_matched_count(self, db_connection):
    """
    # count matched media
    """
    return await db_connection.fetchval('select count(*) from mm_media'
                                        ' where mm_media_metadata_guid is not NULL')


async def db_media_new(self, db_connection, offset=None, records=None, search_value=None,
                       days_old=7):
    """
    # new media
    """
    if offset is None:
        return await db_connection.fetch('select mm_media_name,'
                                         ' mm_media_guid,'
                                         ' mm_media_class_guid'
                                         ' from mm_media, mm_metadata_movie'
                                         ' where mm_media_metadata_guid = mm_metadata_guid'
                                         ' and mm_media_json->>\'DateAdded\' >= $1'
                                         ' order by LOWER(mm_media_name),'
                                         ' mm_media_class_guid',
                                         (datetime.datetime.now()
                                          - datetime.timedelta(days=days_old)).strftime(
                                             "%Y-%m-%d"))
    else:
        return await db_connection.fetch('select mm_media_name,'
                                         ' mm_media_guid,'
                                         ' mm_media_class_guid'
                                         ' from mm_media, mm_metadata_movie'
                                         ' where mm_media_metadata_guid = mm_metadata_guid'
                                         ' and mm_media_json->>\'DateAdded\' >= $1'
                                         ' order by LOWER(mm_media_name),'
                                         ' mm_media_class_guid offset $2 limit $3',
                                         (datetime.datetime.now()
                                          - datetime.timedelta(days=days_old)).strftime(
                                             "%Y-%m-%d"),
                                         offset, records)


async def db_media_new_count(self, db_connection, search_value=None, days_old=7):
    """
    # new media count
    """
    return await db_connection.fetchval('select count(*) from mm_media, mm_metadata_movie'
                                        ' where mm_media_metadata_guid = mm_metadata_guid'
                                        ' and mm_media_json->>\'DateAdded\' >= $1',
                                        (datetime.datetime.now()
                                         - datetime.timedelta(days=days_old)).strftime(
                                            "%Y-%m-%d"))


async def db_media_path_by_uuid(self, db_connection, media_uuid):
    """
    # find path for media by uuid
    """
    return await db_connection.fetchval('select mm_media_path from mm_media'
                                        ' where mm_media_guid = $1',
                                        media_uuid)


async def db_media_rating_update(self, db_connection, media_guid, user_id, status_text):
    """
    # set favorite status for media
    """
    if status_text == 'watched' or status_text == 'mismatch':
        status_setting = True
    else:
        status_setting = status_text
        status_text = 'Rating'
    try:
        json_data = await db_connection.fetchval('SELECT mm_media_json from mm_media'
                                                 ' where mm_media_guid = $1 FOR UPDATE',
                                                 media_guid)
        if 'UserStats' not in json_data:
            json_data['UserStats'] = {}
        if user_id in json_data['UserStats']:
            json_data['UserStats'][user_id][status_text] = status_setting
        else:
            json_data['UserStats'][user_id] = {status_text: status_setting}
        # TODO since 'for update' must release record on fail
        self.db_update_media_json(db_connection, media_guid, json.dumps(json_data))
        self.db_commit()
    except:
        self.db_rollback()
        return None


async def db_media_unmatched_list(self, db_connection, offset=0, list_limit=None):
    return await db_connection.fetch('select mm_media_guid,'
                                     ' mm_media_path from mm_media'
                                     ' where mm_media_metadata_guid is NULL'
                                     ' order by mm_media_path offset $1 limit $2',
                                     offset, list_limit)


async def db_media_unmatched_list_count(self, db_connection):
    return await db_connection.fetchval('select count(*) from mm_media'
                                        ' where mm_media_metadata_guid is NULL')
