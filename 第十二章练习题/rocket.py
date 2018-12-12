import pygame

class Rocket():

	def __init__(self, screen):
		"""初始化火箭并设置其初始位置"""
		self.screen = screen
		
		# 加载火箭图像并获取其外接矩形
		self.image = pygame.image.load('images/rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# 将每只新火箭放在屏幕中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
	def blitme(self):
		"""在指定位置绘制火箭"""
		self.screen.blit(self.image, self.rect)
