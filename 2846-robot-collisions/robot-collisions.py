class Robot:
    def __init__(self, position, health, direction, index):
        self.position = position
        self.health = health
        self.direction = direction
        self.index = index


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        robots = [
            Robot(p, h, d, i)
            for i, (p, h, d) in enumerate(zip(positions, healths, directions))
        ]
        robots.sort(key=lambda x: x.position)

        n = len(positions)
        result = [0] * n  # the health of surviving robots
        stack = []

        for robot in robots:
            if robot.direction == "R":
                stack.append(robot)
            else:  # 'L'
                while stack and robot.health > 0:
                    r = stack.pop()
                    if r.health < robot.health:
                        # r is destroyed
                        robot.health -= 1
                    elif r.health > robot.health:
                        # robot is destroyed
                        r.health -= 1
                        stack.append(r)
                        break
                    else:
                        robot.health = 0
                        break
                else:
                    result[robot.index] = robot.health

        while stack:
            r = stack.pop()
            result[r.index] = r.health

        return [h for h in result if h > 0]
