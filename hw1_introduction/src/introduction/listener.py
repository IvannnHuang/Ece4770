import numpy as np
import rospy

# BEGIN QUESTION 4.3
from geometry_msgs.msg import PoseStamped
# END QUESTION 4.3


def norm_python(data):
    """Compute the norm for each row of a numpy array using Python for loops.

    >>> data = np.array([[3, 4],
    ...                  [5, 12]])
    >>> norm_python(data)
    array([ 7., 17.])
    """
    n, d = data.shape
    norm = np.zeros(n)
    # BEGIN QUESTION 4.1
    for i in range(n):
        sum_sq = 0
        for j in range(d):
            sum_sq += np.absolute(data[i, j])
        norm[i] = sum_sq
    # END QUESTION 4.1
    return norm


def norm_numpy(data):
    """Compute the norm for each row of a numpy array using numpy functions.

    >>> data = np.array([[3, 4],
    ...                  [5, 12]])
    >>> norm_numpy(data)
    array([ 7., 17.])
    """
    # BEGIN QUESTION 4.2
    norm = np.linalg.norm(data, ord=1, axis=1)
    norm[norm == 0] = 1.0
    # END QUESTION 4.2
    return norm


class PoseListener:
    """Collect car poses."""

    def __init__(self, size=100):
        self.size = size
        self.done = False
        self.storage = []  # a list of (x, y) tuples
        # Create a subscriber for the car pose.
        # BEGIN QUESTION 4.3
        self.subscriber = rospy.Subscriber("/car/car_pose", PoseStamped, self.callback)
        # END QUESTION 4.3

    def callback(self, msg):
        """Store the x and y coordinates of the car."""
        header = msg.header
        rospy.loginfo(
            "Received a new message with timestamp " + str(header.stamp.secs) + "(s)"
        )

        # Extract and store the x and y position from the message data
        # BEGIN QUESTION 4.4
        x = msg.pose.position.x
        y = msg.pose.position.y
        self.storage.append((x, y))
        # END QUESTION 4.4
        
        if len(self.storage) == self.size:
            self.done = True
            rospy.loginfo("Received enough samples, trying to unsubscribe")
            self.subscriber.unregister()
