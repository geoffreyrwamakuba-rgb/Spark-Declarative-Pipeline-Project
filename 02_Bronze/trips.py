#from pyspark.sql import functions as F
from pyspark.sql.functions import *
from pyspark import pipelines as dp

source_path = "s3://goodcabs-gr/data-store/trips"
# readStream -- read data in a stream style - only new files are read when this is run
# This is an auto loader feature
# Without autoloader you need to manually create separate files for new vs processed vs fail 

@dp.table(
    name = "transportation.bronze.trips",
    comment = "Streaming ingestion of raw orders with Auto loader",
    table_properties = {
        'quality':'bronze',
        'layer':'bronze',
        'source_format':'csv',
        'delta.enableChangeDataFeed':'true',
        'delta.autoOptimize.optimizeWrite':'true',
        'delta.autoOptimize.autoCompact':'true'}
    )
def trips_bronze():
    df = (spark.readStream.format("cloudFiles")
        .option("cloudFiles.format","csv")
        .option("cloudFiles.inferColumnTypes","true")
        .option("cloudFiles.schemaEvolutionMode","rescue")
        # No failure with scheam changes --> rescue column created, (like mode=PERMISSIVE with spark.read)
        .option("cloudFiles.maxFilesPerTrigger",100)
        #Max of 100 files processed in this run 
        .load(source_path)
        )
    df = df.withColumnRenamed("distance_travelled(km)","distance_travelled_km")
    df = (df.withColumn("file_name",col("_metadata.file_path"))
          .withColumn("ingest_datetime",current_timestamp()))
    return df

