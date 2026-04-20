
from pyspark import pipelines as dp
from pyspark.sql.functions import *

source_path = "s3://goodcabs-gr/data-store/city"

# define function with decaroator
# Writing @my_decorator is just a cleaner way of saying: 
# say_hello = my_decorator(say_hello), used for timers and "boilerplate" code

# This approach will save you time as imperattive gets more complicated 

# @dp.materialized_view is for batch data and materialized views
# @dp.table is for streaming tables with incremental updates

@dp.materialized_view(
    name ="transportation.bronze.city",
    comment = "City Raw Data Processing",
    table_properties = {
        'quality' : 'bronze',
        'layer' : 'bronze',
       'source_format' : "csv",
       'delta.enableChangeDataFeed' : 'true', 
       'delta.autoOptimize.optimizeWrite' : 'true', 
       'delta.autoOptimize.autoCompact' : 'true'}
    )
def city_bronze():
    df = (spark.read.format("csv")
          .option("header","true")
          .option("inferSchema","true")
          .option("mergeSchema","true")
          .option("mode","PERMISSIVE") # vs FAILFAST
          .option("columnNameOfCorruptRecord","_corrupt_record")
          .load(source_path))
    
    df = (df.withColumn("file_name",col("_metadata.file_path")).
          withColumn("ingest_datetime",current_timestamp()))
    
    return df
          

