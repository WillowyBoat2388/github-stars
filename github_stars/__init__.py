from dagster import (
    load_assets_from_modules,
    Definitions,
    define_asset_job,
    ScheduleDefinition,
)
from . import assets
from .resources import github_api
import os
from github import Github

defs = Definitions(
    assets=load_assets_from_modules([assets], group_name='GITHUB_ASSETS'),
    schedules=[
        ScheduleDefinition(
            job=define_asset_job(name="daily_refresh", selection="*"),
            cron_schedule="@daily",
        )
    ],
    resources={"github_api": Github(os.environ["GITHUB_ACCESS_TOKEN"]),
            #    "github_api1": github_api.configured({"access_token": {"env": "GITHUB_ACCESS_TOKEN"}})
               },
)

# from dagster import Definitions, load_assets_from_modules

# from . import assets

# all_assets = load_assets_from_modules([assets])

# defs = Definitions(
#     assets=all_assets,
# )
