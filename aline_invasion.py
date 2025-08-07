import sys

import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screent = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("外星人入侵")

        # 设置背景颜色
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screent.fill(self.bg_color)

            # 最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
