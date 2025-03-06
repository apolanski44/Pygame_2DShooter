# 2D Shooter Game

A simple 2D shooter game built with Pygame, where the player defends against waves of enemies in an arena. The game includes various levels, bosses, bonuses, and an event loop for handling user input and game mechanics.

## Features
- Defend against enemies on an arena.
- Multiple levels with increasing difficulty.
- Boss fights at the end of certain levels.
- Bonuses to help the player.
- Simple event loop to manage game flow.

## Classes

### Bonus
The base class for all bonus items in the game. Handles the positioning, drawing, and interaction with the player.

- `__init__(self, image, x, y, player)` - Initializes the bonus with an image, position (x, y), and the player object.
- `draw(self, surface)` - Draws the bonus image on the game surface.

### hp_potion (Inherits from Bonus)
A health potion bonus that increases the player's health when collected.

- `__init__(self, image, x, y, player)` - Initializes the health potion.
- `col_with_player(self)` - Checks for collision with the player and, if not used, plays a sound and increases the player's health by 100.
- `update(self)` - Calls `col_with_player` to handle collisions.

### speed_potion (Inherits from Bonus)
A speed potion bonus that increases the player's speed when collected.

- `__init__(self, image, x, y, player)` - Initializes the speed potion.
- `col_with_player(self)` - Checks for collision with the player and, if not used, plays a sound and increases the player's speed by 1.
- `update(self)` - Calls `col_with_player` to handle collisions.

### Bullet
The class for the bullet object in the game, responsible for its movement and lifetime.

- `__init__(self, bullet_image, x, y, angle)` - Initializes the bullet with an image, position (x, y), and angle. Sets the initial speed and calculates the velocity in the x and y directions based on the angle.
- `bullet_movement(self)` - Updates the bullet's position based on its velocity. Also checks if the bullet has lived for longer than its lifetime and destroys it if necessary.
- `update(self, *args)` - Calls `bullet_movement` to update the bullet's position each frame.

### Button
A class for creating interactive buttons in the game, allowing users to click and trigger actions.

- `__init__(self, image, x, y)` - Initializes the button with an image, position (x, y), and creates a rectangle for collision detection. Sets the initial state of the button as inactive.
- `draw(self, surface)` - Draws the button on the screen. It checks if the mouse is hovering over the button and if the button is clicked. Returns `True` if the button is clicked.
- `set_active(self, state)` - Sets the active state of the button (either active or inactive). Resets the clicked state when the button's active status changes.

### Enemy
A base class for all enemy types in the game, responsible for movement, collision detection, and damage handling.

- `__init__(self, image, cx, cy, player, obstacles)` - Initializes the enemy with an image, position (cx, cy), player, and obstacles.
- `draw(self, surface)` - Draws the enemy on the screen.
- `hunt(self)` - Moves the enemy towards the player and handles attacking logic when in range.
- `col_with_obstacles(self)` - Checks for collisions with obstacles and adjusts the enemy's speed accordingly.
- `update(self, surface)` - Updates the enemy’s movement and collision logic.
- `get_distance(self, vectorP, vectorE)` - Calculates the distance between the player and the enemy.
- `get_dmg(self)` - Checks if the enemy is hit by a bullet and applies damage. If the enemy’s health reaches zero, it plays a death sound and adds points to the player.

### Zombie1 (Inherits from Enemy)
A basic zombie enemy with moderate health and attack damage.

- `__init__(self, image, cx, cy, player, obstacles)` - Initializes the zombie with specific health, speed, attack damage, and cooldown.

### Zombie2 (Inherits from Enemy)
A stronger zombie enemy with more health and higher attack damage.

- `__init__(self, image, cx, cy, player, obstacles)` - Initializes the zombie with specific health, speed, attack damage, and cooldown.

### Headless (Inherits from Enemy)
A mid-tier enemy with balanced stats, including moderate health and attack damage.

- `__init__(self, image, cx, cy, player, obstacles)` - Initializes the headless enemy with specific health, speed, attack damage, and cooldown.

### Boss1 (Inherits from Enemy)
A stronger boss enemy with high health and significant damage. Displays a health bar.

- `__init__(self, image, cx, cy, player, obstacles)` - Initializes the boss with high health, attack damage, and cooldown.
- `draw_health_bar(self, surface)` - Draws the boss's health bar on the screen.

### Boss2 (Inherits from Enemy)
The second boss enemy, much stronger with a significantly higher health pool and damage.

- `__init__(self, image, cx, cy, player, obstacles)` - Initializes the boss with very high health, attack damage, and cooldown.
- `draw_health_bar(self, surface)` - Draws the boss's health bar on the screen.

## `Level` Class
The base class for levels in the game, responsible for managing enemies, bonuses, and obstacles within the level.

### Attributes:
- `player`: The player object that interacts with the level.
- `images`: A dictionary containing images used within the level.
- `boss_spawned`: A flag indicating whether the boss has been spawned.
- `boss`: The boss object that appears in the level.
- `boss_defeated`: A flag indicating whether the boss has been defeated.
- `enemy_group`: A sprite group containing enemies within the level.
- `bonus_group`: A sprite group containing bonuses within the level.
- `text`: The "wave cleared" text displayed after defeating the boss.
- `text_rect`: The rectangle for positioning the "wave cleared" text.
- `is_played`: A flag indicating whether the music has been played.
- `obstacles`: A list of obstacles in the level, represented as rectangles.

### Methods:
- `draw(surface)`: Draws enemies and bonuses on the screen.
- `reset()`: Resets the player's state and the level (e.g., restoring health, clearing enemy and bonus groups).
  
---

## `Level_1` Class
The first level of the game.

### Additional Attributes:
- `speed_potion_used`: A flag indicating whether the speed potion has been used.
- `hp_potion_used`: A flag indicating whether the health potion has been used.
- `music`: The music played during the boss fight.

### Methods:
- `update(surface)`: Updates the level by spawning enemies, managing bonuses, and handling the boss fight.
  - Spawns enemies when there are less than 4.
  - Adds bonuses based on the player's points.
  - Spawns the boss when the player's points reach a certain threshold (10 points).
  - Plays music when the boss fight starts.
  - Displays a "wave cleared" message and resets the level after the boss is defeated.

---

## `Level_2` Class
The second level of the game, similar to `Level_1` but with increased difficulty.

### Additional Attributes:
- `speed_potion_used`: A flag indicating whether the speed potion has been used.
- `hp_potion_used`: A flag indicating whether the health potion has been used.
- `music`: The music played during the boss fight.

### Methods:
- `update(surface)`: Updates the level similarly to `Level_1`, but with adjustments for the second level:
  - Spawns more powerful enemies.
  - Adds bonuses based on the player's points.
  - Spawns the boss when the player's points reach a certain threshold (10 points).
  - Plays music during the boss fight.
  - Displays a "wave cleared" message and resets the level after the boss is defeated.

 # `Player` Class

The `Player` class represents the player character in the game. It handles player movement, rotation, shooting, health, and collision with obstacles. The class also manages the player's score and health bar display.

## Attributes:
- **base_image**: The base image used for the player.
- **image**: The current image (rotated) of the player.
- **rect**: The rectangle object that defines the player’s position and size on the screen.
- **shoot_cooldown**: The cooldown time between each shot (in frames).
- **points**: The player's current score.
- **obstacles**: The list of obstacles that the player must avoid.
- **hp**: The player's current health.
- **speed**: The player's movement speed.
- **max_hp**: The maximum health of the player.
- **attack_damage**: The damage dealt by the player's attacks.
- **bullet_group**: A sprite group that contains all bullets fired by the player.
- **gun_offset**: A `Vector2` representing the offset for the gun’s position relative to the player.
- **collision_rect**: A rectangle used for detecting collisions with obstacles.
- **mouse_pos**: The position of the mouse cursor.
- **x_change_mouse_player**: The change in the x-axis between the mouse and player’s center.
- **y_change_mouse_player**: The change in the y-axis between the mouse and player’s center.
- **angle**: The angle of rotation for the player based on the mouse position.

## Methods:
### `draw_health_bar(surface)`
Draws the health bar on the given surface. It displays the player's current health in green and the remaining health bar in red.

### `draw_points(surface, font)`
Displays the player's current score (points) on the screen at a specified position.

### `update_collision_rect()`
Updates the position of the player's collision rectangle to match the player's position.

### `draw(surface)`
Draws the player’s image on the given surface at its current position.

### `shoot()`
Fires a bullet from the player. The bullet is fired when the player clicks the left mouse button, and the cooldown timer ensures the player cannot shoot too rapidly.

### `player_rotation()`
Rotates the player’s image to face the mouse cursor. The player’s image is updated to point towards the mouse position.

### `col_with_obstacles()`
Checks if the player’s collision rectangle intersects with any of the obstacles. Returns `True` if a collision occurs, otherwise `False`.

### `update(key_pressed)`
Updates the player's state, including movement and shooting, based on the current keys pressed and the player's position. It also checks for collisions with obstacles and keeps the player within the bounds of the screen.

### `get_event(key_pressed)`
Handles player movement by checking if the respective keys (`A`, `D`, `W`, `S`) are pressed. It also checks for shooting when the left mouse button is clicked.
