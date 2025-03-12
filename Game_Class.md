# :video_game: Exercise: Build Your Own Game Class (No Inheritance or Polymorphism)
## **:memo: Instructions**
In this exercise, you will **create a simple RPG battle system** using **basic Object-Oriented Programming (OOP) principles** in Python.
### **:pushpin: Requirements**
1. **Create a `Character` class** with:
   - `name` (string) – The character's name
   - `health` (integer) – The character's health points (HP)
   - `attack_power` (integer) – The character's attack damage
   - A method **`attack(target)`** that reduces `target.health`
2. **Encapsulate `health` as a private variable**
   - Add a **getter method** (`get_health()`) to access the character’s health.
   - Add a **setter method** (`take_damage(damage)`) to reduce health safely.
3. **Create two different characters** and make them fight each other.
   - Loop through turns where **one attacks the other until one reaches 0 HP**.
   - Print the attack logs and remaining health.
---
## **:desktop_computer: Starter Code (Fill in the TODOs)**
```python
import time
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        # TODO: Make health a private variable
        self.attack_power = attack_power
    def attack(self, target):
        # TODO: Print an attack message
        # TODO: Call the target's take_damage method
    def get_health(self):
        # TODO: Return the private health variable
    def take_damage(self, damage):
        # TODO: Reduce health by the damage amount, but not below 0
        # TODO: Print how much health is left
# TODO: Create two characters (player and enemy)
# TODO: Simulate a battle loop
while player.get_health() > 0 and enemy.get_health() > 0:
    # TODO: Player attacks enemy
    # TODO: Check if enemy is defeated, if yes, break the loop
    time.sleep(1)  # Add delay for readability
    # TODO: Enemy attacks player
    # TODO: Check if player is defeated, if yes, break the loop
    time.sleep(1)  # Add delay for readability

