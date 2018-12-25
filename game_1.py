import random
class Creature_boss_and_player():
	def __init__(self,hp,name):
		self.hp = hp
		self.name = name

	def attack_D(self):
		attack_vaule_d = random.randint(0,70)
		return attack_vaule_d

	def attack_P(self):
		attcak_vaule_p = random.randint(0,85)
		return attack_vaule_p

	def attack_boss(self):
		attcak_vaule_boss = random.randint(0,80)
		return attcak_vaule_boss

	def becoming(self,attacking):
		self.hp = self.hp - attacking

	def show_table(self):
		print("{}\'s hp is {}\t.".format(self.name,self.hp))
		print('*'*(int)(self.hp/10))

	def not_dead(self):
		if self.hp>0:
			return True

class Creatrue_small():

	def __init__(self,hp,name):
		self.hp = hp
		self.name = name

	def attcak_small(self):
		attack_vaule = random.randint(0,40)
		return attack_vaule

	def becoming(self,attacking):
		self.hp = self.hp - attacking

	def show_table(self):
		print("{}\'s hp is {}\t.".format(self.name,self.hp))
		print('*'*(int)(self.hp/10))

	def not_dead(self):
		if self.hp>0:
			return True

player_d = Creature_boss_and_player(500,'you')
player_p = Creature_boss_and_player(380,'you')
enemy_small1 = Creatrue_small(40,'enemy_small1')
enemy_small2 = Creatrue_small(40,'enemy_small2')
enemy_boss = Creature_boss_and_player(160,'enemy_boss')

player = input("choose your body(D/P):")

if player == 'D':
	while player_d.not_dead() and enemy_boss.not_dead():
		player_d.show_table()
		enemy_boss.show_table()
		enemy_small1.show_table()
		enemy_small2.show_table()
		while True:
			user_input = input("Attack or Defence(A/D)")
			if user_input == 'A':
				break
			elif user_input == 'D':
				break
		if enemy_small2.not_dead() or enemy_small1.not_dead():
			if user_input == 'A':
				player_attack_vaule = player_d.attack_D()
				enemy_small1_attack_vaule = enemy_small1.attcak_small()
				enemy_small2_attack_vaule = enemy_small2.attcak_small()
				player_attack_vaule1 = random.randint(0,player_attack_vaule)
				player_attack_vaule2 = player_attack_vaule - player_attack_vaule1
				player_d.becoming(enemy_small1_attack_vaule)
				player_d.becoming(enemy_small2_attack_vaule)
				enemy_small1.becoming(player_attack_vaule1)
				enemy_small2.becoming(player_attack_vaule2)
			elif user_input == 'D':
				enemy_small1_attack_vaule = enemy_small1.attcak_small()*0.1
				player_d.becoming(enemy_small1_attack_vaule)
				player_d.becoming(enemy_small2_attack_vaule)#两个怪物的时候
		else:
			if user_input == 'A':
				player_attack_vaule = player_d.attack_D()
				enemy_boss_attack_vaule = enemy_boss.attack_boss()
				player_d.becoming(enemy_boss_attack_vaule)
				enemy_boss.becoming(player_attack_vaule)
			elif user_input == 'D':
				enemy_boss_attack_vaule = enemy_boss.attcak_boss()*0.1
				player_d.becoming(enemy_boss_attack_vaule)



elif player == 'P':
	while player_p.not_dead() and enemy_boss.not_dead():
		player_p.show_table()
		enemy_boss.show_table()
		enemy_small1.show_table()
		enemy_small2.show_table()
		while True:
			user_input = input("Attack or Defence(A/D)")
			if user_input == 'A':
				break
			elif user_input == 'D':
				break
		if enemy_small2.not_dead() or enemy_small1.not_dead():
			if user_input == 'A':
				player_attack_vaule = player_p.attack_D()
				enemy_small1_attack_vaule = enemy_small1.attcak_small()
				enemy_small2_attack_vaule = enemy_small2.attcak_small()
				player_attack_vaule1 = random.randint(0,player_attack_vaule)
				player_attack_vaule2 = player_attack_vaule - player_attack_vaule1
				player_p.becoming(enemy_small1_attack_vaule)
				player_p.becoming(enemy_small2_attack_vaule)
				enemy_small1.becoming(player_attack_vaule1)
				enemy_small2.becoming(player_attack_vaule2)
			elif user_input == 'D':
				enemy_small1_attack_vaule = enemy_small1.attcak_small()*0.1
				player_p.becoming(enemy_small1_attack_vaule)
				player_p.becoming(enemy_small2_attack_vaule)#两个怪物的时候
		else:
			if user_input == 'A':
				player_attack_vaule = player_p.attack_D()
				enemy_boss_attack_vaule = enemy_boss.attack_boss()
				player_p.becoming(enemy_boss_attack_vaule)
				enemy_boss.becoming(player_attack_vaule)
			elif user_input == 'D':
				enemy_boss_attack_vaule = enemy_boss.attcak_boss()*0.1
				player_p.becoming(enemy_boss_attack_vaule)


if player == 'D':
	print("$\n")
	if player_d.not_dead():
		print("you win!\n")
	else:
		print("you lose!\n")
else:
	if player_d.not_dead():
		print("you win!\n")
	else:
		print("you lose!\n")


				
			
			


