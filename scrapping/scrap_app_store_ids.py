from itunes_app_scraper.scraper import AppStoreScraper
from tqdm.auto import tqdm

if __name__ == "__main__":
    ids = []
    scraper = AppStoreScraper()

    for collection in tqdm(
        [
            "newapplications",
            "newfreeapplications",
            "newpaidapplications",
            "topfreeapplications",
            "topfreeipadapplications",
            "topgrossingapplications",
            "topgrossingipadapplications",
            "toppaidapplications",
            "toppaidipadapplications",
        ]
    ):
        for country in tqdm(
            [
                "us",
                "de",
                "ca",
                "gb",
                "nl",
            ]
        ):
            try:
                res = scraper.get_app_ids_for_collection(collection=collection, num=500, country=country)
            except Exception as e:
                print(e)
                continue
            for item in res:
                ids.append(item)

    ids = set(ids)

    with open("app_store_ids.txt", "w") as file:
        file.write("\n".join(ids))

    print("Done")
