from typing import Sequence

from pydantic import Field

from biodata_registry_api.models.crud import Page, PageFilter
from biodata_registry_api.models.views import DataAssetView
from fastapi_filter.contrib.sqlalchemy import Filter

class DataAssetViewsPage(Page):
    results: Sequence[DataAssetView]

class DataAssetViewsFilter(PageFilter):
    data_asset_id: int | None = Field(default=None)
    acquisition_id: int | None = Field(default=None)
    instrument_id: int | None = Field(default=None)
    instrument_name__ilike: str | None = Field(default=None)
    data_asset_name__ilike: str | None = Field(default=None)
    data_asset_location__ilike: str | None = Field(default=None)
    class Constants(Filter.Constants):
        model = DataAssetView
