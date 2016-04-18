from unittest import TestCase
from games import snake


class AppTest(TestCase):

    def setUp(self):
        self.cls = snake.Snake()

    def test_array(self):
        self.cls.MAX_COLUMNS = 3
        self.cls.MAX_ROWS = 3
        self.cls.fruit = [2, 2]
        assert self.cls.array() == [
            ['0', '0', '>'],
            ['.', '.', '.'],
            ['.', '.', 'X']
        ]

    def test_new_fruit(self):
        self.cls.new_fruit()
        self.assertTrue(self.cls.fruit not in self.cls.player)

    def test_eat(self):
        self.cls.player[0] = [2,2]
        self.cls.fruit = [2,2]
        self.cls.eat([1,1])
        self.assertEqual(len(self.cls.player), 4)

    def test_swap(self):
        self.cls.swap()
        self.assertEqual(self.cls.player, [[0, 2], [0, 2], [0, 1]])

    def test_just_do_it(self):
        self.cls.just_do_it()
        self.assertEqual(self.cls.last_part, self.cls.player[len(self.cls.player)-1])

    def test_control(self):
        self.cls.player = [[0, 2], [0, 1], [0, 0]]  # row, column
        self.cls.control('s')
        self.assertEqual(self.cls.direction, 'S')
        self.cls.control('a')
        self.assertEqual(self.cls.direction, 'W')
        self.cls.control('w')
        self.assertEqual(self.cls.direction, 'N')
        self.cls.control('d')
        self.assertEqual(self.cls.direction, 'E')
