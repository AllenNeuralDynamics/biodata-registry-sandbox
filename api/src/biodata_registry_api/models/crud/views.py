from typing import Sequence
from biodata_registry_api.models.crud import Page, PageFilter
from biodata_registry_api.models.views import DataAssetView

class DataAssetViewsPage(Page):
    results: Sequence[DataAssetView]

class DataAssetViewsFilter(PageFilter):
    data_asset_id: int | None = None
    acquisition_id: int | None = None
    instrument_id: int | None = None
    instrument_name__ilike: str | None = None
    data_asset_name__ilike: str | None = None
    data_asset_location__ilike: str | None = None
    class Constants:
        model = DataAssetView
