
import json
from collections import OrderedDict
import chardet


def detect_encoding(filename):
    with open(filename, "rb") as f:
        return chardet.detect(f.read())


def read_json_file(filename):
    file_encoding = detect_encoding(filename)
    print("Detected encoding:", file_encoding['encoding'])
    with open(filename, "r", encoding=file_encoding['encoding']) as f:
        content = f.read()

        data = json.loads(content)
        return data


def recursively_sort(data, k=''):
    order = []
    if not k:
        order = ['DataVersion', 'Manufacturer', 'ManufacturerID', 'FixtureName', 'FixtureID', 'ShortName', 'Category',
                 'Description', 'DengkuID', 'Physical', 'Logicals',
                 'DMXModes', 'Revisions']
    elif k == 'Revisions':
        order = ['Date', 'ModifiedBy', 'Text', 'UserID', 'BaseOnVersion']
    elif k == 'DMXModes':
        order = ['Name', 'DMXFootprint', 'Description', 'DMXChannels']
    elif k == 'DMXChannels':
        order = ['Name', 'BelongsToLogicalPixel', 'Offset', 'DMXChannels']
    elif k == 'LogicalChannel':
        order = ['Attribute', 'ChannelFunction']
    elif k == 'ChannelFunction':
        order = ['Name', 'Default', 'CustomName', 'PhysicalFrom', 'PhysicalTo', 'ChannelSet']
    elif k == 'ChannelSet':
        order = ['Name', 'DMXFrom', 'DMXTo', 'MappingFrom', 'MappingTo', 'WheelSlot']
    elif k == 'Physical':
        order = ['PhysicalPixelFootprint', 'PhysicalHeight', 'PhysicalWidth', 'PhysicalDepth', 'Outlines', 'PhysicalPixels']
    elif k == 'Logicals':
        order = ['MappingDMXMode', 'PixelFootprint', 'LogicalPixels']
    elif k == 'Outlines' or k == 'PhysicalPixels' or k == 'LogicalPixels':
        order = ['OutlineName', 'PhysicalPixelName', 'LogicalPixelName', 'Index', 'Shape', 'X', 'Y', 'Height', 'Width', 'Radius', 'BorderWidth', 'BorderColor', 'FillColor', 'FontText', 'FontX', 'FontY', 'FontPixelSize', 'MappingPhysicalPixel']
    else:
        ...

    if isinstance(data, dict):
        sorted_data = OrderedDict()
        for key in order:
            if key in data:
                sorted_data[key] = recursively_sort(data[key], key)
        for key in data:
            if key not in order:
                sorted_data[key] = recursively_sort(data[key], key)
        return sorted_data
    if isinstance(data, list):
        print(k)
        return [recursively_sort(item, k) for item in data]
    return data


if __name__ == '__main__':
    # filename = '../NGTF/15X - main.json'
    filename = '../NGTF/15X - description.json'
    d = read_json_file(filename)

    sorted_dict = recursively_sort(d)

    print('sorted_dict: ', sorted_dict)
    ordered_data = OrderedDict(sorted_dict)

    with open('example_output.json', 'w') as file:
        json.dump(ordered_data, file, indent=4)
