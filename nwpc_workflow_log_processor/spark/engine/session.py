# coding: utf-8
import findspark
from pyspark.sql import SparkSession
from pyspark import SparkConf


def create_spark_session(config: dict) -> SparkSession:
    engine_config = config["engine"]

    findspark.init(engine_config["spark_home"])
    config_pairs = list(engine_config["spark_config"].items())
    conf = SparkConf().setAll(config_pairs)
    spark = SparkSession \
        .builder \
        .appName(engine_config["app_name"]) \
        .master("local[4]") \
        .config(conf=conf) \
        .getOrCreate()
    spark.sparkContext.setLogLevel(engine_config["log_level"])
    return spark
