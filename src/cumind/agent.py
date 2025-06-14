"""CuMind agent implementation."""

from typing import Any, Dict, List, Tuple

import numpy as np
import torch
import torch.nn.functional as functional

from .config import CuMindConfig
from .mcts import MCTS
from .network import CuMindNetwork


class CuMindAgent:
    """CuMind agent for training and inference."""

    def __init__(self, config: CuMindConfig):
        """Initialize CuMind agent with network, optimizer, and MCTS.

        Args:
            config: CuMindConfig with network architecture and training parameters

        Implementation:
            - Create CuMindNetwork with config parameters
            - Setup Adam optimizer with learning rate and weight decay
            - Initialize MCTS instance for action selection
        """
        # Branch: feature/agent-initialization
        raise NotImplementedError("__init__ needs to be implemented")

    def select_action(self, observation: np.ndarray, training: bool = True) -> int:
        """Select action using MCTS search from current observation.

        Args:
            observation: Current game state observation
            training: If True, sample from action probabilities; if False, take best action

        Returns:
            Selected action index

        Implementation:
            - Convert observation to tensor and run network.initial_inference()
            - Use MCTS to search and get action probabilities
            - Sample action if training, else take argmax
        """
        # Branch: feature/mcts-action-selection
        raise NotImplementedError("select_action needs to be implemented")

    def train_step(self, batch: List[Any]) -> Dict[str, float]:
        """Perform one training step on a batch of replay data.

        Args:
            batch: List of game trajectories from replay buffer

        Returns:
            Dictionary of loss values for monitoring

        Implementation:
            - Call _prepare_batch() to extract observations, actions, targets
            - Call _compute_losses() to get loss dictionary
            - Sum losses, run backward pass with optimizer step
            - Return loss values as float dict for logging
        """
        # Branch: feature/training-step
        raise NotImplementedError("train_step needs to be implemented")

    def _prepare_batch(self, batch: List[Any]) -> Tuple[torch.Tensor, torch.Tensor, Dict[str, torch.Tensor]]:
        """Extract and format training data from replay buffer batch.

        Args:
            batch: Raw batch data from replay buffer

        Returns:
            Tuple of (observations, actions, targets) tensors ready for training

        Implementation:
            - Parse batch format (depends on your replay buffer structure)
            - Extract observations, action sequences, and CuMind targets
            - Convert to appropriate tensor shapes and types
            - Target dict should have "values", "rewards", "policies" keys
        """
        # Branch: feature/batch-preparation
        raise NotImplementedError("_prepare_batch needs to be implemented")

    def _compute_losses(
        self,
        observations: torch.Tensor,
        actions: torch.Tensor,
        targets: Dict[str, torch.Tensor],
    ) -> Dict[str, torch.Tensor]:
        """Compute CuMind losses for value, policy, and reward predictions.

        Args:
            observations: Batch observations, shape (batch_size, *obs_shape)
            actions: Action sequences, shape (batch_size, num_unroll_steps)
            targets: Dict with "values", "policies", "rewards" target tensors

        Returns:
            Dict of loss tensors: {"value_loss", "policy_loss", "reward_loss"}

        Implementation:
            - Run initial_inference() on observations
            - Unroll dynamics with recurrent_inference() for each action
            - Compute MSE loss for values/rewards, cross-entropy for policies
            - Average losses across unroll steps
        """
        # Branch: feature/loss-computation
        raise NotImplementedError("_compute_losses needs to be implemented")

    def save_checkpoint(self, path: str) -> None:
        """Save model checkpoint with network weights, optimizer state, and config.

        Args:
            path: File path to save checkpoint

        Implementation:
            - Use torch.save() to save dict with network state_dict,
              optimizer state_dict, and config
        """
        # Branch: feature/checkpoint-saving
        raise NotImplementedError("save_checkpoint needs to be implemented")

    def load_checkpoint(self, path: str) -> None:
        """Load model checkpoint to restore training state.

        Args:
            path: File path to load checkpoint from

        Implementation:
            - Use torch.load() to load checkpoint dict
            - Restore network and optimizer state_dicts
        """
        # Branch: feature/checkpoint-loading
        raise NotImplementedError("load_checkpoint needs to be implemented")
