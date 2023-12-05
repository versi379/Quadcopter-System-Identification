#!/usr/bin/env python3
import rosbag
import argparse


def log_extractor(bag_file, topic, output_file_dir):
    print("Extracting Logs from topic {}".format(topic))

    file = open(output_file_dir, "w")
    first_raw = True

    for topic, msg, t in bag_file.read_messages(topics=topic):
        key_values = msg.status[0].values
        keys = []
        values = []
        for kv in key_values:
            keys.append(kv.key)
            values.append(kv.value)

        if first_raw:
            file.write(",".join(keys)+"\n")
            first_raw = False

        file.write(",".join(values)+"\n")

    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract Logs from a rosbag.")
    parser.add_argument("bag_file", help="Input ROS bag.", type=str)
    parser.add_argument("output_file", help="Output file (csv).", type=str)
    parser.add_argument("--topic", help="Diagnostics Topic", type=str, required=False, default="/diagnostics")

    args = parser.parse_args()

    bag = rosbag.Bag(args.bag_file, "r")

    log_extractor(bag, args.topic, args.output_file)
