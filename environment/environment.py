import numpy as np

class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)  # Initialize grid with zeros
        self.pickup_cells = [(1, 5), (2, 4), (5, 2)]  # Initial pickup cells
        self.dropoff_cells = [(1, 1), (3, 1), (4, 5)]  # Initial dropoff cells
        self.block_capacity = 5
        self.agents = {'red': (3, 3), 'blue': (3, 5), 'black': (1, 3)}  # Initial agent positions
        
        # Initialize blocks in pickup cells
        for cell in self.pickup_cells:
            self.grid[cell] = self.block_capacity
            
    def reset(self):
        self.grid = np.zeros((self.size, self.size), dtype=int)  # Reset grid
        # Reinitialize pickup cells with blocks
        for cell in self.pickup_cells:
            self.grid[cell] = self.block_capacity
        # Reset agent positions
        self.agents = {'red': (3, 3), 'blue': (3, 5), 'black': (1, 3)}

    def move_agent(self, agent, direction):
        dx, dy = direction
        x, y = self.agents[agent]
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            # Check if the new position is not occupied by another agent
            if all((new_x, new_y) != pos for pos in self.agents.values()):
                self.agents[agent] = (new_x, new_y)
    
    def pickup_blocks(self, agent):
        x, y = self.agents[agent]
        if (x, y) in self.pickup_cells:
            self.grid[x, y] -= 1
            return 1  # Reward for successful pickup
        else:
            return 0  # No reward for unsuccessful pickup
    
    def dropoff_blocks(self, agent):
        x, y = self.agents[agent]
        if (x, y) in self.dropoff_cells:
            self.grid[x, y] += 1
            return 1  # Reward for successful dropoff
        else:
            return 0  # No reward for unsuccessful dropoff
    
    def is_terminal_state(self):
        for cell in self.dropoff_cells:
            if self.grid[cell] != self.block_capacity:
                return False
        return True

# Main simulation loop
if __name__ == "__main__":
    env = GridWorld()
    # Perform actions in the environment
    # Example:
    # 1. Move agent 'red' to the east
    env.move_agent('red', (0, 1))
    # 2. Pickup blocks with agent 'blue'
    reward = env.pickup_blocks('blue')
    print("Reward for pickup:", reward)
    # 3. Dropoff blocks with agent 'black'
    reward = env.dropoff_blocks('black')
    print("Reward for dropoff:", reward)
