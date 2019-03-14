import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=64, fc2_units=64):
        """Initialize parameters and build model.
        Params
        ======
            model for p1 navigation
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        self.fc = nn.Sequential(nn.Linear(state_size, 128), nn.ReLU())
        self.advantage = nn.Sequential(nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, action_size))
        self.value = nn.Sequential(nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, 1))

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = self.fc(state)
        G = self.value(x) + self.advantage(x) - self.advantage(x).mean()
        return G
