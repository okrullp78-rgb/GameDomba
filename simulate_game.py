#!/usr/bin/env python3
"""Simulasi sederhana ekonomi & progression GameDomba"""
import random

# Konfigurasi ekonomi & mekanik (tweak these)
WIN_CREDIT_MIN = 10
WIN_CREDIT_MAX = 50
PREMIUM_FOOD_DROP_CHANCE = 0.05
BASIC_FOOD_PRICE = 1
PREMIUM_FOOD_PRICE = 20
TOURNAMENT_ENTRY = 20

class Sheep:
    def __init__(self, name="Domba", age_months=6):
        self.name = name
        self.age = age_months
        self.level = 1
        self.xp = 0
        self.stamina = 80
        self.strength = 10
        self.speed = 10
        self.mood = 80

    def feed(self, food_type='basic'):
        if food_type == 'basic':
            self.stamina = min(100, self.stamina + 15)
        elif food_type == 'premium':
            self.stamina = min(100, self.stamina + 35)
            self.xp += 5

    def train(self, intensity=1):
        cost = 10 * intensity
        if self.stamina < cost:
            return False
        self.stamina -= cost
        gained_xp = 5 * intensity
        self.xp += gained_xp
        self.strength += 1 * intensity
        self.speed += 0.5 * intensity
        if self.xp >= 20 * self.level:
            self.level += 1
            self.xp = 0
        return True

    def compete(self, opponent_level):
        my_score = self.strength * 0.6 + self.speed * 0.4 + random.uniform(0, 10)
        opp_base = opponent_level * 5
        opp_score = opp_base + random.uniform(0, 10)
        return my_score >= opp_score


def simulate_run(rounds=20):
    credits = 100
    inventory = {'basic_food': 5, 'premium_food': 0}
    sheep = Sheep('SiBulu')

    for r in range(1, rounds + 1):
        print(f"--- Round {r} ---")
        # Decide action: if low stamina, feed; else train; occasionally compete
        if sheep.stamina < 30 and inventory['basic_food'] > 0:
            sheep.feed('basic')
            inventory['basic_food'] -= 1
            print(f"Fed basic food. Stamina: {sheep.stamina}")
        else:
            trained = sheep.train(intensity=1)
            print(f"Trained: {trained}. Level: {sheep.level}, Strength: {sheep.strength:.1f}, Stamina: {sheep.stamina}")

        # 30% chance to enter match
        if random.random() < 0.3:
            opp_lvl = max(1, sheep.level + random.choice([-1, 0, 1]))
            win = sheep.compete(opp_lvl)
            if win:
                gain = random.randint(WIN_CREDIT_MIN, WIN_CREDIT_MAX)
                credits += gain
                # drop items
                if random.random() < PREMIUM_FOOD_DROP_CHANCE:
                    inventory['premium_food'] += 1
                    print(f"Menang! Dapat {gain} credits dan 1 premium food")
                else:
                    inventory['basic_food'] += 1
                    print(f"Menang! Dapat {gain} credits dan 1 basic food")
            else:
                print("Kalah, tidak dapat reward.")

        # Simple shop auto-buy basic food if low
        if inventory['basic_food'] < 2 and credits >= BASIC_FOOD_PRICE:
            buy_qty = min(5, credits // BASIC_FOOD_PRICE)
            inventory['basic_food'] += buy_qty
            credits -= buy_qty * BASIC_FOOD_PRICE
            print(f"Beli {buy_qty} basic food. Credits left: {credits}")

        # small natural regen
        sheep.stamina = min(100, sheep.stamina + 5)

        print(f"Credits: {credits}, Inventory: {inventory}\n")

    print("--- Simulasi selesai ---")
    print(f"Final: Level {sheep.level}, Strength {sheep.strength:.1f}, Credits {credits}, Inventory {inventory}")


if __name__ == '__main__':
    simulate_run(30)
