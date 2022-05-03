class Horse(object):
    def __init__(self, ar, point):

        a = [[0 for j in range(ar)] for i in range(ar)]
        matrix = [[0 for j in range(ar * ar)] for i in range(ar * ar)]

        k = 1
        for i in range(ar):
            for j in range(ar):
                a[i][j] = k
                k += 1

        self.dom = a

        def is_normal(i, j):
            if 0 <= i < ar and 0 <= j < ar:
                return True
            else:
                return False

        s = []

        for i in range(0, ar):
            for j in range(0, ar):
                if is_normal(i + 1, j + 2):
                    matrix[i * ar + j][(i + 1) * ar + (j + 2)] = 1
                if is_normal(i - 1, j - 2):
                    matrix[i * ar + j][(i - 1) * ar + (j - 2)] = 1
                if is_normal(i + 1, j - 2):
                    matrix[i * ar + j][(i + 1) * ar + (j - 2)] = 1
                if is_normal(i - 1, j + 2):
                    matrix[i * ar + j][(i - 1) * ar + (j + 2)] = 1
                if is_normal(i + 2, j + 1):
                    matrix[i * ar + j][(i + 2) * ar + (j + 1)] = 1
                if is_normal(i - 2, j - 1):
                    matrix[i * ar + j][(i - 2) * ar + (j - 1)] = 1
                if is_normal(i + 2, j - 1):
                    matrix[i * ar + j][(i + 2) * ar + (j - 1)] = 1
                if is_normal(i - 2, j + 1):
                    matrix[i * ar + j][(i - 2) * ar + (j + 1)] = 1

        visited = []
        voavrat = 0

        def Neighbors(point):
            t = matrix[point - 1]

            neighbors = []
            for i in range(0, ar * ar):
                if t[i] == 1:
                    neighbors.append(i + 1)

            return neighbors

        def chngnei(point, visit):
            neighbors = Neighbors(point)
            a = [[] for i in range(len(neighbors))]
            for i in range(len(neighbors)):
                a[i].append(neighbors[i])
                new_neighbors = Neighbors(neighbors[i])
                k = len(new_neighbors)
                for j in new_neighbors:
                    if j in visit:
                        k -= 1
                a[i].append(k)
            a.sort(key=lambda x: x[1])
            res = []
            for x in a:
                res.append(x[0])
            return res

        visited.append(point)
        bad = [[] for i in range(ar * ar + 1)]

        while True:
            if len(visited) == ar * ar:
                self.hody = visited
                break
            Flag = True
            for x in chngnei(point, visited):
                if (x not in visited) and (x not in bad[point]):
                    visited.append(x)
                    Flag = False
                    break

            if Flag:
                bad[visited[len(visited) - 2]].append(point)
                del visited[len(visited) - 1]
                voavrat += 1
                bad[point].clear()
                point = visited[len(visited) - 1]
                try:
                    point = visited[len(visited) - 1]
                except IndexError:
                    exit()
            else:
                point = visited[len(visited) - 1]

    def get_result(self):
        return self.hody
