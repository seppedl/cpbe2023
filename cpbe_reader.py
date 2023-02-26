"""
Read projects
"""
from requests import get
import pandas as pd


url = "https://backend.coolestprojects.be/website/planning/3/projects.json"

response = get(url=url)
if response.status_code == 200:
    temp = response.json()
    df = pd.DataFrame.from_dict(temp)
    df.to_excel("CPBE_2023.xlsx", index=False)
