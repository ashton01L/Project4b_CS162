# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Write a Box class whose init method takes three parameters and uses them to initialize the private
# length, width and height data members of a Box.
class Box:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        return self._length * self._width * self._height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


def box_sort(box_list):
    """
    Sorts a list of Box objects in-place from greatest volume to least volume.
    """
    for i in range(1, len(box_list)):
        key_box = box_list[i]
        key_volume = key_box.volume()
        j = i - 1
        # Shift elements of box_list[0..i-1] that are smaller than key_volume
        # to one position ahead of their current position
        while j >= 0 and box_list[j].volume() < key_volume:
            box_list[j + 1] = box_list[j]
            j -= 1
        box_list[j + 1] = key_box


# Test
# b1 = Box(3.4, 19.8, 2.1)
# b2 = Box(1.0, 1.0, 1.0)
# b3 = Box(8.2, 8.2, 4.5)
# box_list = [b1, b2, b3]
# box_sort(box_list)

# Display sorted volumes to confirm
# for box in box_list:
#     print(f"Box with volume: {box.volume()}")