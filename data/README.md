# Data

## Source

[Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) on Kaggle.

## Download

```bash
# Requires Kaggle API credentials at ~/.kaggle/kaggle.json
kaggle datasets download -d olistbr/brazilian-ecommerce -p data/raw --unzip
```

Expected files in `data/raw/`:

- `olist_customers_dataset.csv`
- `olist_geolocation_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`
- `product_category_name_translation.csv`

## Versioning

Raw data is tracked with DVC (not committed to git). After download:

```bash
dvc add data/raw
```
