from pyspark.sql.functions import * 
#from pyspark.sql import functions as F
from pyspark import pipelines as dp

# View created for the quality checks  
@dp.temporary_view(
    name="trips_silver_staging",
    comment="Tranformed trips data ready for CDC upsert"
)
# Expectations will do checks and create error logs not stop the processing
# there is also dp.expect_or_drop() , dp.expect_or_fail()
@dp.expect("valid_date","year(business_date) >=2020")
@dp.expect("valid_driver_rating","driver_rating BETWEEN 1 AND 10")
@dp.expect("valid_passenger_rating","passenger_rating BETWEEN 1 AND 10")
def trips_silver():
    df_bronze = spark.readStream.table("transportation.bronze.trips") 

    df_silver = df_bronze.withColumn("passenger_type", lower(col("passenger_type")))

    df_silver = df_silver.select(
        col("trip_id").alias("id"),
        col("date").cast("date").alias("business_date"),
        col("city_id").alias("city_id"),
        col("passenger_type").alias("passenger_category"),
        col("distance_travelled_km").alias("distance_kms"),
        col("fare_amount").alias("sales_amt"),
        col("passenger_rating").alias("passenger_rating"),
        col("driver_rating").alias("driver_rating"),
        col("ingest_datetime").alias("bronze_ingest_timestamp"),
    )

    df_silver = df_silver.withColumn(
        "silver_processed_timestamp", current_timestamp()
    )
    return df_silver




