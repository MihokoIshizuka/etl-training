#!/usr/bin/env python
# coding: utf-8
import sys
import argparse
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
import json


def main():

    # spark sessionの作成
    spark = SparkSession.builder \
    .appName("etl") \
    .config("hive.exec.dynamic.partition", "true") \
    .config("hive.exec.dynamic.partition.mode", "nonstrict") \
    .config("spark.sql.session.timeZone", "JST") \
    .config("spark.ui.enabled","true") \
    .config("spark.eventLog.enabled","false") \
    .enableHiveSupport() \
    .getOrCreate()

    # parquetの読み込み
    df=spark.read.parquet("/tmp/share_file/datalake/people/")
    # テンポラリ
    df.createOrReplaceTempView("hoge")
    # string型のデータをembulkで取得するとbinary型となってしまうため、一度StringにCastしないといけない。
    result = spark.sql("select cast(name as string) , cast(email as string), id, cast(source as string) from hoge")
    result.coalesce(1).write.mode('overwrite').csv("/tmp/share_file/datamart/people/")

    # 最後は停止処理をします
    spark.stop()

if __name__ == '__main__':
    main()
