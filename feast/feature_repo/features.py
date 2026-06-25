"""Feast feature definitions — implement after dbt marts are ready."""

from datetime import timedelta

from feast import Entity, FeatureView, Field, ValueType
from feast.types import Float64, Int64

customer = Entity(name="customer", join_keys=["customer_id"])

# Placeholder feature view; fields will match dbt mart columns.
user_features = FeatureView(
    name="user_features",
    entities=[customer],
    ttl=timedelta(days=7),
    schema=[
        Field(name="user_total_orders", dtype=Int64),
        Field(name="user_avg_order_value", dtype=Float64),
    ],
    source=None,  # Wire to Postgres source after dbt models exist
)
