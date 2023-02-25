from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "artful-turbine-378406.pizza_delivery.orders"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("order_id", "INTEGER"),
        bigquery.SchemaField("customer_id", "INTEGER"),
        bigquery.SchemaField("type", "STRING"),
        bigquery.SchemaField("qty", "INTEGER"),
        bigquery.SchemaField("retail_price", "FLOAT"),
        bigquery.SchemaField("order_date", "DATETIME"),
    ],
    skip_leading_rows=0, # skip "header rows"!
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://artful-turbine-378406/orders.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))
