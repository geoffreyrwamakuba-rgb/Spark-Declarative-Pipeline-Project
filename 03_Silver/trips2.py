from pyspark.sql.functions import * 
#from pyspark.sql import functions as F
from pyspark import pipelines as dp

# Not a decorator like @dp.table
# Can be useful when combining multuple streams/tables
dp.create_streaming_table(
    name ="transportation.silver.trips",
    comment = "Cleaned and standardized trips fact processing",
    table_properties = {
        'quality' : 'silver',
        'layer' : 'silver',
        'delta.enableChangeDataFeed' : 'true', 
        'delta.autoOptimize.optimizeWrite' : 'true', 
        'delta.autoOptimize.autoCompact' : 'true'}
    )

# move data from view to the streaming table we have made
# upsert approach
dp.create_auto_cdc_flow(
    target = "transportation.silver.trips",
    source = "trips_silver_staging",
    keys=["id"],  # condition, if this matches update, if not insert
    sequence_by = "silver_processed_timestamp",
    stored_as_scd_type = 1, # overwrites vs 2 which keeps old + new rows with start and end date
    except_column_list=[] # exclude columns of choice
)
