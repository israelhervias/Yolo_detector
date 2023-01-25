import unittest
import ejercicio6

class TestGroupImagesByFolder(unittest.TestCase):
    def test_correct_number_of_images(self):
        folder_path = "dataset_cities/images"
        n_clusters = 2

        result = ejercicio6.group_images_by_folder(folder_path, n_clusters)

        count_zurich_images = 0
        for image_name in result:
            if image_name.startswith("zurich"):
                count_zurich_images += 1

        self.assertEqual(count_zurich_images, len(result))

if __name__ == '__main__':
    unittest.main()


