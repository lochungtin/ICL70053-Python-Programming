import json
import sys


def load_json(filename):
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)

    return data


def merge_annotations(dataset):
    image_annotations = {}
    for annotation in dataset["annotations"]:
        id = annotation["image_id"]
        if id not in image_annotations:
            image_annotations[id] = []

        image_annotations[id].append(
            {"id": annotation["id"], "bbox": annotation["bbox"]}
        )

    for image in dataset["images"]:
        image.update({"annotations": image_annotations[image["id"]]})

    return dataset["images"]


def save_data(filename, data):
    with open(filename, "w+") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    dataset = load_json("lesson9/" + sys.argv[1])
    merged = merge_annotations(dataset)
    save_data("lesson9/" + sys.argv[2], merged)
