from pydantic import ConfigDict
from src.schemas.base.anomaly_base import AnomalyBase


class AnomalyResponse(AnomalyBase):

    model_config = ConfigDict(from_attributes=True)
