// launch the vs tools app otherwise can't compile (windows os only)
use serde_json::{Value};
use std::error::Error;
use std::env;
use std::collections::HashMap;
//use serde::{Deserialize, Serialize};

#[path = "../../mk_lib_common/src/mk_lib_common.rs"]
mod mk_lib_common;
#[path = "../../mk_lib_compression/src/mk_lib_compression.rs"]
mod mk_lib_compression;
#[path = "../../mk_lib_database/src/mk_lib_database.rs"]
mod mk_lib_database;
#[path = "../../mk_lib_database/src/mk_lib_database_metadata.rs"]
mod mk_lib_database_metadata;
#[path = "../../mk_lib_logging/src/mk_lib_logging.rs"]
mod mk_lib_logging;
#[path = "../../mk_lib_network/src/mk_lib_network.rs"]
mod mk_lib_networks;

#[derive(Serialize, Deserialize)]
struct Metadata {
    media_id: u8,
    adult_media: bool,
}

fn main() -> Result<(), Box<dyn Error>> {
    // start logging
    mk_lib_logging::mk_logging_post_elk("info",
                                        "START",
                                        "bulk_themoviedb_netfetch");

    let fetch_date: String = "06_10_2021".to_string();

    // // open the database
    let dp_pass = env::var("POSTGRES_PASSWORD").unwrap();
    let db_client = mk_lib_database::mk_lib_database_open(&dp_pass);

    // grab the movie id's
    let _fetch_result = mk_lib_networks::mk_download_file_from_url(
        format!("http://files.tmdb.org/p/exports/movie_ids_{}.json.gz", fetch_date),
        "movie.gz".to_string());
    let json_result = mk_lib_compression::mk_decompress_gzip("movie.gz").unwrap();
    // Parse the string of data into serde_json::Value.
    for json_item in json_result.split('\n') {
        //let p: Metadata = serde_json::from_str(json_item)?;
        let json_line: HashMap<String, Value> = serde_json::from_str(&json_item)?;
        println!("{:?}, {:?}", json_line["id"], json_line["adult"]);
        if mk_lib_database_metadata::mk_lib_database_metadata_exists_movie(db_client,
                                                                           &json_line["id"]) {

        }
    }

    // grab the TV id's
    let _fetch_result = mk_lib_networks::mk_download_file_from_url(
        format!("http://files.tmdb.org/p/exports/tv_series_ids_{}.json.gz", fetch_date),
        "tv.gz".to_string());
    let json_result = mk_lib_compression::mk_decompress_gzip("tv.gz").unwrap();
    // Parse the string of data into serde_json::Value.
    for json_item in json_result.split('\n') {
        let json_line: HashMap<String, Value> = serde_json::from_str(&json_item)?;
        println!("{:?}, {:?}", json_line["id"], json_line["adult"]);
    }




    // let name = "Ferris";
    // let data = None::<&[u8]>;
    // client.execute(
    //     "INSERT INTO person (name, data) VALUES ($1, $2)",
    //     &[&name, &data],
    // )?;
    //
    // for row in client.query("SELECT id, name, data FROM person", &[])? {
    //     let id: i32 = row.get(0);
    //     let name: &str = row.get(1);
    //     let data: Option<&[u8]> = row.get(2);
    //     println!("found person: {} {} {:?}", id, name, data);
    // }

    // stop logging
    mk_lib_logging::mk_logging_post_elk("info",
                                        "STOP",
                                        "bulk_themoviedb_netfetch");
    Ok(())
}