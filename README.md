Overview

This is a simple command-line implementation of the classic UNO card game in Python. The game supports two players and includes basic UNO gameplay mechanics, such as matching cards by color or number, turn-based play, and action cards like Wilds and Draw Twos.

Features

Two-player gameplay: A simplified version of UNO for two-four players.

Turn-based mechanics: Players take turns drawing and playing cards.

Matching rules: Play a card that matches the current color or number.

Action cards: Includes Wild cards, skips, reverses and Draw Two cards with special effects.

Winner detection: The game declares a winner when a player has no cards left.

How to Play

Each player starts with a set number of cards.

Players take turns playing a valid card or drawing if no valid move is available.

Action cards trigger special effects:

Draw Two/Draw Four: Forces the next player to draw two cards and skip their turn.
Reverse: Reverses the direction of player order.
Skip: Skips next players turn.
Wild: Allows the player to choose a new color.

The first player to run out of cards wins the game.
