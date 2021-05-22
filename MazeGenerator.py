import random

class MazeGenerator:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.path = []
        self.start_point = []
        self.dead_ends = []
        self.goal = 0
        self.n = 1

    def sinir_kontrol(self, point):
        if point[0] > self.width - 40 or point[0] < 0 or point[1] > self.height - 40 or point[1] < 0:
            return True
        else:
            return False

    def baslangic_noktasi_olustur(self):
        right_bound = int((self.width - 80) / 40)
        x = random.randint(1, right_bound)
        while x % 2 == 0:
            x = random.randint(1, right_bound)

        top_bound = int((self.height - 80) / 40)
        y = random.randint(1, top_bound)
        while y % 2 == 0:
            y = random.randint(1, top_bound)

        self.start_point = [x * 40, y * 40]

    def yol_olustur(self, current_point, pathway):
        while True:
            if pathway.count([current_point[0] + 80, current_point[1]]) == 1 or self.sinir_kontrol(
                    [current_point[0] + 80, current_point[1]]):
                if pathway.count([current_point[0] - 80, current_point[1]]) == 1 or self.sinir_kontrol(
                        [current_point[0] - 80, current_point[1]]):
                    if pathway.count([current_point[0], current_point[1] + 80]) == 1 or self.sinir_kontrol(
                            [current_point[0], current_point[1] + 80]):
                        if pathway.count([current_point[0], current_point[1] - 80]) == 1 or self.sinir_kontrol(
                                [current_point[0], current_point[1] - 80]):
                            self.dead_ends.append(current_point)
                            if self.n == 1:
                                self.goal = current_point
                                self.n = 0
                            return pathway

            x = random.randint(1, 4)

            test_point = [current_point[0], current_point[1]]
            if x == 1:
                test_point[0] += 80
                if pathway.count(test_point) == 1 or self.sinir_kontrol(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0] - 40, test_point[1]])

            elif x == 2:
                test_point[0] -= 80
                if pathway.count(test_point) == 1 or self.sinir_kontrol(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0] + 40, test_point[1]])

            elif x == 3:
                test_point[1] += 80
                if pathway.count(test_point) == 1 or self.sinir_kontrol(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0], test_point[1] - 40])

            elif x == 4:
                test_point[1] -= 80
                if pathway.count(test_point) == 1 or self.sinir_kontrol(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0], test_point[1] + 40])

            pathway = self.yol_olustur(current_point, pathway)

    def hedefi_tekrar_tanımla(self):
        p = random.randint(1, len(self.dead_ends) - 1)
        return self.dead_ends[p]

    def labirent_olustur(self):
        """Returns the coordinates of points for the normal tiles, the starting point, and the goal"""
        self.baslangic_noktasi_olustur()
        pathway = [self.start_point]
        self.path = self.yol_olustur(self.start_point, pathway)

        return self.path, self.start_point, self.goal
