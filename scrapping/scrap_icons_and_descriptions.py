import pandas as pd
from itunes_app_scraper.scraper import AppStoreScraper
from joblib import Parallel, delayed
from tqdm.auto import tqdm


def scarp_the_id(id):
    id = id.strip(" \n")
    try:
        info = scrapper.get_app_details(id, country="us")
    except KeyboardInterrupt:
        raise BaseException("Cancel!!!!")
    except Exception as e:
        try:
            info = scrapper.get_app_details(id, country="uk")
        except Exception as e:
            try:
                info = scrapper.get_app_details(id, country="de")
            except Exception as e:
                return None

    icon_link = info["artworkUrl512"]
    description = info["description"]
    tags = info["genres"]
    app_name = info["trackName"]
    prince = info["formattedPrice"]

    return icon_link, description, tags, app_name, prince


if __name__ == "__main__":
    with open("app_store_ids.txt") as file:
        ids = file.readlines()

    scrapper = AppStoreScraper()
    data = []

    res = Parallel(n_jobs=12)(delayed(scarp_the_id)(id) for id in tqdm(ids))
    print(f"There are {len(res)} apps")

    for id in res:
        if id is not None:
            data.append(id)

    data = pd.DataFrame(data, columns=["icon_link", "description", "tags", "app_name", "price"])
    data.to_csv("app_store_dump.csv", index=False)

    print("Done")
