import sys

sys.path.append("../")
from utils import get_center_of_bbox, measure_distance


class PlayerBallAssigner:
    def __init__(self):
        self.max_player_ball_distance = (
            70  # Adjust based on experimentation for accuracy
        )

    def assign_ball_to_player(self, players, ball_bbox):
        ball_position = get_center_of_bbox(ball_bbox)

        min_distance = float("inf")  # Minimum distance starts at infinity
        assigned_player = -1

        for player_id, player in players.items():
            player_bbox = player["bbox"]

            # Calculate the center of the player's bounding box
            player_center = get_center_of_bbox(player_bbox)

            # Measure distances from multiple key points on the player bbox
            distances = [
                measure_distance(
                    (player_bbox[0], player_bbox[1]), ball_position
                ),  # Top-left
                measure_distance(
                    (player_bbox[2], player_bbox[1]), ball_position
                ),  # Top-right
                measure_distance(
                    (player_bbox[0], player_bbox[3]), ball_position
                ),  # Bottom-left
                measure_distance(
                    (player_bbox[2], player_bbox[3]), ball_position
                ),  # Bottom-right
                measure_distance(player_center, ball_position),  # Center of bbox
            ]

            # Find the minimum distance to the ball among these points
            min_player_distance = min(distances)

            # Assign the ball to the nearest player if within the threshold
            if min_player_distance < self.max_player_ball_distance:
                if min_player_distance < min_distance:
                    min_distance = min_player_distance
                    assigned_player = player_id

        return assigned_player
