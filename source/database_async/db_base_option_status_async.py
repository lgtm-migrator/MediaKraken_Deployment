import json


async def db_opt_update(self, db_connection, option_json):
    """
    Update option json
    """
    # no need for where clause as it's only the one record
    await db_connection.execute('update mm_options_and_status'
                                ' set mm_options_json = $1',
                                option_json)


async def db_opt_json_read(self, db_connection):
    """
    Read options
    """
    json_result = await db_connection.fetchval(
        'select mm_options_json'
        ' from mm_options_and_status')
    print(json_result, flush=True)
    return json.loads(json_result)


async def db_status_json_read(self, db_connection):
    """
    Read options
    """
    return json.loads(await db_connection.fetchval(
        'select mm_status_json'
        ' from mm_options_and_status')['mm_status_json'])
