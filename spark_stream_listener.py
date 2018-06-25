from pyspark.sql.functions import col
from pyspark.sql import SQLContext, SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from collections import namedtuple
# from pyspark.sql.functions import desc

sc = SparkContext("local[2]", "Tweet Streaming App")


ssc = StreamingContext(sc, 10)
sqlContext = SQLContext(sc)
#ssc.checkpoint( "file:/home/ubuntu/tweets/checkpoint/")

socket_stream = ssc.socketTextStream("ec2-18-191-228-213.us-east-2.compute.amazonaws.com", 2323) # Internal ip of  the tweepy streamer

lines = socket_stream.window(20)
lines.pprint()
fields = ("SentimentText")
Tweet = namedtuple( 'Tweet', fields )

def getSparkSessionInstance(sparkConf):
    if ("sparkSessionSingletonInstance" not in globals()):
        globals()["sparkSessionSingletonInstance"] = SparkSession \
            .builder \
            .config(conf=sparkConf) \
            .getOrCreate()
    return globals()["sparkSessionSingletonInstance"]

def do_something(time, rdd):
    print("========= %s =========" % str(time))
    try:
        # Get the singleton instance of SparkSession
        spark = getSparkSessionInstance(rdd.context.getConf())

        # Convert RDD[String] to RDD[Tweet] to DataFrame
        rowRdd = rdd.map(lambda w: Tweet(w))
        linesDataFrame = spark.createDataFrame(rowRdd)

        # Creates a temporary view using the DataFrame
        linesDataFrame.createOrReplaceTempView("tweets")

        # Do tweet character count on table using SQL and print it
        lineCountsDataFrame = spark.sql("select SentimentText, length(SentimentText) as TextLength from tweets")
        lineCountsDataFrame.show()
        lineCountsDataFrame.coalesce(1).write.format("com.databricks.spark.csv").save("/home/ubuntu/server/tweetcapture2")
    except:
        pass


# key part!
lines.foreachRDD(do_something)

ssc.start()
ssc.awaitTermination()


