import subprocess
import pandas as pd
from tqdm.auto import tqdm
from joblib import Parallel, delayed


def download(df, idx):
    out_path = f"icons/{idx}_{df['app_name'][idx]}.jpg"

    for bad_char in [" ", ":", "&", "@", "'", "`", '"', "!", "?"]:
        out_path = out_path.replace(bad_char, "_")

    command = f"wget {df['icon_link'][idx]} -O {out_path}"
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    df = pd.read_csv("app_store_dump.csv")

    Parallel(n_jobs=12)(delayed(download)(df, idx) for idx in tqdm(range(len(df["icon_link"]))))

    print("Done")
